"""
Models for Product

All of the models are stored in this module
"""
import logging
from flask_sqlalchemy import SQLAlchemy
import json
import logging
from cloudant.client import Cloudant
from cloudant.query import Query
from cloudant.adapters import Replay429Adapter
from requests import HTTPError, ConnectionError

logger = logging.getLogger("flask.app")

# Create the SQLAlchemy object to be initialized later in init_db()
db = SQLAlchemy()

# get configruation from enviuronment (12-factor)
ADMIN_PARTY = os.environ.get('ADMIN_PARTY', 'False').lower() == 'true'
CLOUDANT_HOST = os.environ.get('CLOUDANT_HOST', 'localhost')
CLOUDANT_USERNAME = os.environ.get('CLOUDANT_USERNAME', 'admin')
CLOUDANT_PASSWORD = os.environ.get('CLOUDANT_PASSWORD', 'pass')

# global variables for retry (must be int)
RETRY_COUNT = int(os.environ.get('RETRY_COUNT', 10))
RETRY_DELAY = int(os.environ.get('RETRY_DELAY', 1))
RETRY_BACKOFF = int(os.environ.get('RETRY_BACKOFF', 2))

class DatabaseConnectionError(Exception):
    """ Custom Exception when database connection fails """
    pass

class DataValidationError(Exception):
    """ Custom Exception with data validation fails """
    pass

class Pet(object):
    """ Pet interface to database """

    logger = logging.getLogger(__name__)
    client = None   # cloudant.client.Cloudant
    database = None # cloudant.database.CloudantDatabase

    def __init__(self, name=None, category=None, available=True):
        """ Constructor """
        self.id = None
        self.name = name
        self.category = category
        self.available = available

# class Product(db.Model):
#     """
#     Class that represents a product
#     """

#     app = None

#     # Table Schema
#     id = db.Column(db.Integer, primary_key=True)
#     sku = db.Column(db.Integer, nullable=False)
#     name = db.Column(db.String(63), nullable=False)
#     category = db.Column(db.String(63), nullable=False)
#     short_description = db.Column(db.String(63), nullable=False)
#     long_description = db.Column(db.String(100))
#     price = db.Column(db.Integer, nullable=False)
#     rating = db.Column(db.Integer)
#     available = db.Column(db.Boolean, nullable=False)
#     enabled = db.Column(db.Boolean, nullable=False)
#     likes = db.Column(db.Integer)

    def __repr__(self):
        return "<Product %r id=[%s]>" % (self.name, self.id)

    def create(self):
        """
        Creates a Product to the database
        """
        logger.info("Creating %s", self.name)
        self.id = None  # id must be none to generate next primary key
        db.session.add(self)
        db.session.commit()

        try:
            document = self.database.create_document(self.serialize())
        except HTTPError as err:
            Pet.logger.warning('Create failed: %s', err)
            return

        if document.exists():
            self.id = document['_id']

    def save(self):
        """
        Updates a Product to the database
        """
        logger.info("Saving %s", self.name)
        db.session.commit()

    def delete(self):
        """ Removes a Product from the data store """
        logger.info("Deleting %s", self.name)
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        """ Serializes a Product into a dictionary """
        return {
            "id": self.id,
            "sku": self.sku,
            "name": self.name,
            "category": self.category,
            "short_description": self.short_description,
            "long_description": self.long_description,
            "price": self.price,
            "rating": self.rating,
            "available": self.available,
            "enabled": self.enabled,
            "likes": self.likes
        }

    def deserialize(self, data):
        """
        Deserializes a Product from a dictionary

        Args:
            data (dict): A dictionary containing the resource data
        """
        try:
            self.sku = data["sku"]
            self.name = data["name"]
            self.category = data["category"]
            self.short_description = data["short_description"]
            self.long_description = data.get("long_description")
            self.price = data["price"]
            self.rating = data.get("rating")
            self.available = data.get("available")
            self.enabled = data.get("enabled")
            self.likes = data.get("likes")
        except KeyError as error:
            raise DataValidationError("Invalid Product: missing " + error.args[0])
        except TypeError as error:
            raise DataValidationError(
                "Invalid Product: body of request contained" "bad or no data"
            )
        return self

    @classmethod
    def init_db(cls, app):
        """ Initializes the database session """
        logger.info("Initializing database")
        cls.app = app
        # This is where we initialize SQLAlchemy from the Flask app
        db.init_app(app)
        app.app_context().push()
        db.create_all()  # make our sqlalchemy tables

    @classmethod
    def all(cls):
        """ Returns all of the Products in the database """
        logger.info("Processing all Products")
        return cls.query.all()

    @classmethod
    def find(cls, by_id):
        """ Finds a Product by it's ID """
        logger.info("Processing lookup for id %s ...", by_id)
        return cls.query.get(by_id)

    @classmethod
    def find_or_404(cls, by_id):
        """ Find a Product by it's id """
        logger.info("Processing lookup or 404 for id %s ...", by_id)
        return cls.query.get_or_404(by_id)

    @classmethod
    def find_by_name(cls, name):
        """ Returns all Products with the given name

        Args:
            name (string): the name of the Products you want to match
        """
        logger.info("Processing name query for %s ...", name)
        return cls.query.filter(cls.name == name)

    @classmethod
    def find_by_category(cls, category):
        """Returns all of the Products in a category
        Args:
            category (string): the category of the Products you want to match
        """
        logger.info("Processing category query for %s ...", category)
        return cls.query.filter(cls.category == category)

    @classmethod
    def find_by_available(cls, available):
        """Returns all of the Products with the given availability
        Args:
            available (bool): the availability of the Products you want to match
        """
        logger.info("Processing available query for %s ...", available)
        return cls.query.filter(cls.available == available)

    @classmethod
    def find_by_rating(cls, rating):
        """Returns all of the Products with the given rating
        Args:
            rating (integer): the rating of the Products you want to match
        """
        logger.info("Processing rating query for %s ...", rating)
        return cls.query.filter(cls.rating == rating)