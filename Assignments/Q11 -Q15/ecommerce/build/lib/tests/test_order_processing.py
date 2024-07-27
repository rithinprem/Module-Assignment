# tests/test_order_processing.py

import unittest
from ecommerce.order_processing import Order, OrderProcessor

class TestOrderProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = OrderProcessor()

    def test_create_order(self):
        order = Order(1, ["Laptop", "Mouse"])
        self.processor.create_order(order)
        self.assertIn(order, self.processor.get_orders())

if __name__ == '__main__':
    unittest.main()
