"""
Test cases for Product Model

"""
import logging
import unittest
import os
from service.models import Product, DataValidationError, db
from service import app

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
            stock_status=True
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

        # Test product without long description
        product = Product(
            sku="12345",
            name="ABCchocolate", 
            category="food", 
            short_description="dark chocolate",
            price="28",
            rating="4", 
            stock_status=True
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
            stock_status=True
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
            rating="4"
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
            stock_status=False
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

        # Asert that it was assigned an id and shows up in the database
        self.assertNotEqual(product.id, None)
        products = Product.all()
        self.assertEqual(len(products), 1)
