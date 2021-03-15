"""
Product API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import os
import logging
from unittest import TestCase
from unittest.mock import MagicMock, patch
from flask_api import status  # HTTP Status Codes
from service.models import db, Product
from service.routes import app, init_db

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgres://postgres:postgres@localhost:5432/postgres"
)

######################################################################
#  T E S T   C A S E S
######################################################################

class TestProductServer(TestCase):
    """ REST API Server Tests """

    @classmethod
    def setUpClass(cls):
        """ Run once before all tests """
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        init_db()

    def setUp(self):
        """ Runs before each test """
        db.drop_all()  # clean up the last tests
        db.create_all()  # create new tables
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def _create_product(self):
        return Product(
            sku=12345,
            name="ABCchocolate", 
            category="food", 
            short_description="dark chocolate",
            long_description="lindts dark chocolate Christmas limited version",
            price=28,
            rating=4, 
            stock_status=True
        )

######################################################################
#  P L A C E   T E S T   C A S E S   H E R E 
######################################################################
    
    def test_index(self):
        """ Test the Home Page """
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # data = resp.get_json()
        # self.assertEqual(data["name"], "Product REST API Service")

    def test_create_product(self):
        """ Create a new Product """
        test_product = self._create_product()
        logging.debug(test_product)
        resp = self.app.post(
            "/products", json=test_product.serialize(), content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        
        # Make sure location header is set
        location = resp.headers.get("Location", None)
        self.assertIsNotNone(location)

        # Check the data is correct
        new_product = resp.get_json()
        self.assertEqual(new_product["sku"], test_product.sku)
        self.assertEqual(new_product["name"], test_product.name)
        self.assertEqual(new_product["category"], test_product.category)
        self.assertEqual(new_product["short_description"], test_product.short_description)
        self.assertEqual(new_product["long_description"], test_product.long_description)
        self.assertEqual(new_product["price"], test_product.price)
        self.assertEqual(new_product["rating"], test_product.rating)
        self.assertEqual(new_product["stock_status"], test_product.stock_status)

        # ToDo: Uncomment once retrieve product is implemented
        # # Check that the location header was correct
        # resp = self.app.get(location, content_type="application/json")
        # self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # new_product = resp.get_json()
        # self.assertEqual(new_product["sku"], test_product.sku)
        # self.assertEqual(new_product["name"], test_product.name)
        # self.assertEqual(new_product["category"], test_product.category)
        # self.assertEqual(new_product["short_description"], test_product.short_description)
        # self.assertEqual(new_product["long_description"], test_product.long_description)
        # self.assertEqual(new_product["price"], test_product.price)
        # self.assertEqual(new_product["rating"], test_product.rating)
        # self.assertEqual(new_product["stock_status"], test_product.stock_status)

    def test_delete_product(self):
        """ Delete a Product """
        test_product = self._create_product()
        resp = self.app.delete(
            "/products/{}".format(test_product.id), content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(resp.data), 0)
        # make sure they are deleted
        resp = self.app.get(
            "/products/{}".format(test_product.id), content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)