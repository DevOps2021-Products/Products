"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice
from service.models import Product


class ProductFactory(factory.Factory):
    """ Creates fake products """

    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    sku = FuzzyChoice(choices=[1234, 3456, 6789, 4179])
    name = FuzzyChoice(choices=["cheeseburger", "Macbook Pro", "iPhone 12 Pro", "Buzzsaw"])
    category = FuzzyChoice(choices=["food", "computers", "phones", "hardware"])
    available = FuzzyChoice(choices=[True, False])
    price = FuzzyChoice(choices=[100, 10000, 500, 750])
    short_description = FuzzyChoice(choices=["the tastiest food", "the fastest computer", "the shinest new phones", "the tools you need for the job"])
    rating = FuzzyChoice(choices=[1, 2, 3, 4, 5])
    enabled = FuzzyChoice(choices=[True, False])
    likes = FuzzyChoice(choices=[0, 1, 5, 100, 10000, 500, 750])