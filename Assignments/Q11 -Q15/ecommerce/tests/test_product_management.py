# tests/test_product_management.py

import unittest
from Ecommerce.product_management import Product, ProductManager

class TestProductManager(unittest.TestCase):

    def setUp(self):
        self.manager = ProductManager()

    def test_add_product(self):
        product = Product("Laptop", 999.99)
        self.manager.add_product(product)
        self.assertIn(product, self.manager.get_products())

if __name__ == '__main__':
    unittest.main()
