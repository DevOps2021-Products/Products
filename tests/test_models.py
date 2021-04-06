"""
Test cases for Product Model

"""
import logging
import unittest
import os
from werkzeug.exceptions import NotFound
from service.models import Product, DataValidationError, db
from service import app
from .factories import ProductFactory

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgres://postgres:postgres@localhost:5432/postgres"
)

######################################################################
#  P R O D U C T   M O D E L   T E S T   C A S E S
######################################################################

class TestProduct(unittest.TestCase):
    """ Test Cases for Product Model """

    @classmethod
    def setUpClass(cls):
        """ This runs once before the entire test suite """
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        Product.init_db(app)

    def setUp(self):
        """ This runs before each test """
        db.drop_all()  # clean up the last tests
        db.create_all()  # make our sqlalchemy tables

    def tearDown(self):
        """ This runs after each test """
        db.session.remove()
        db.drop_all()

    def _create_product(self):
        return Product(
            sku="12345",
            name="ABCchocolate", 
            category="food", 
            short_description="dark chocolate",
            long_description="lindts dark chocolate Christmas limited version",
            price="28",
            rating="4", 
            stock_status=True,
            enabled = True,
            likes = 10
        )

######################################################################
#  P L A C E   T E S T   C A S E S   H E R E 
######################################################################

    def test_create_a_product(self):
        """ Create a product and assert that it exists """
        product = self._create_product()
        
        self.assertTrue(product != None)
        self.assertEqual(product.id, None)
        self.assertEqual(product.sku, "12345")
        self.assertEqual(product.name, "ABCchocolate")
        self.assertEqual(product.category, "food")
        self.assertEqual(product.short_description, "dark chocolate")
        self.assertEqual(product.long_description, "lindts dark chocolate Christmas limited version")
        self.assertEqual(product.price, "28")
        self.assertEqual(product.rating, "4")
        self.assertEqual(product.stock_status, True)
        self.assertEqual(product.enabled, True)
        self.assertEqual(product.likes, 10)

        # Test product without long description
        product = Product(
            sku="12345",
            name="ABCchocolate", 
            category="food", 
            short_description="dark chocolate",
            price="28",
            rating="4", 
            stock_status=True,
            enabled = True,
            likes = 10
        )
        self.assertTrue(product != None)
        self.assertEqual(product.id, None)
        self.assertEqual(product.long_description, None)

        # Test product without ratings
        product = Product(
            sku="12345",
            name="ABCchocolate", 
            category="food", 
            short_description="dark chocolate",
            long_description="lindts dark chocolate Christmas limited version",
            price="28",
            stock_status=True,
            enabled = True,
            likes = 10
        )
        self.assertTrue(product != None)
        self.assertEqual(product.id, None)
        self.assertEqual(product.rating, None)

        # Test product without stock_status
        product = Product(
            sku="12345",
            name="ABCchocolate", 
            category="food", 
            short_description="dark chocolate",
            long_description="lindts dark chocolate Christmas limited version",
            price="28",
            rating="4",
            enabled = True,
            likes = 10
        )
        self.assertTrue(product != None)
        self.assertEqual(product.id, None)
        self.assertEqual(product.stock_status, None)

        # Test product with stock_status false
        product = Product(
            sku="12345",
            name="ABCchocolate", 
            category="food", 
            short_description="dark chocolate",
            long_description="lindts dark chocolate Christmas limited version",
            price="28",
            rating="4", 
            stock_status=False,
            enabled = True,
            likes = 10
        )
        self.assertTrue(product != None)
        self.assertEqual(product.id, None)
        self.assertEqual(product.stock_status, False)

    def test_add_a_product(self):
        """ Create a product and add it to the database """
        products = Product.all()
        self.assertEqual(products, [])

        product = self._create_product()
        self.assertTrue(product != None)
        self.assertEqual(product.id, None)
        product.create()

        # Assert that it was assigned an id and shows up in the database
        self.assertNotEqual(product.id, None)
        products = Product.all()
        self.assertEqual(len(products), 1)

    def test_find_product(self):
        """ Find a Product by ID """
        products = ProductFactory.create_batch(3)
        for product in products:
            product.create()
        logging.debug(product)
        # make sure they got saved
        self.assertEqual(len(Product.all()), 3)
        # find the 2nd product in the list
        product = Product.find(products[1].id)
        self.assertIsNot(product, None)
        self.assertEqual(product.id, products[1].id)
        self.assertEqual(product.name, products[1].name)
        self.assertEqual(product.stock_status, products[1].stock_status)

    def test_find_or_404_found(self):
        """ Find or return 404 found """
        products = ProductFactory.create_batch(3)
        for product in products:
            product.create()

        product = Product.find_or_404(products[1].id)
        self.assertIsNot(product, None)
        self.assertEqual(product.id, products[1].id)
        self.assertEqual(product.name, products[1].name)
        self.assertEqual(product.stock_status, products[1].stock_status)

    def test_find_or_404_not_found(self):
        """ Find or return 404 NOT found """
        self.assertRaises(NotFound, Product.find_or_404, 0)

    def test_update_a_product(self):
        """ Update a Product """
        product = ProductFactory()
        logging.debug(product)
        product.create()
        logging.debug(product)
        self.assertEqual(product.id, 1)
        # Change it an save it
        product.category = "food"
        original_id = product.id
        product.save()
        self.assertEqual(product.id, original_id)
        self.assertEqual(product.category, "food")
        # Fetch it back and make sure the id hasn't changed
        # but the data did change
        products = Product.all()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].id, 1)
        self.assertEqual(products[0].category, "food")

    def test_delete_a_product(self):
        """ Delete a Product """
        product = self._create_product()
        product.create()
        self.assertEqual(len(Product.all()), 1)
        # delete the product and make sure it isn't in the database
        product.delete()
        self.assertEqual(len(Product.all()), 0)
