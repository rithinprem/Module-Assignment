# ecommerce/order_processing.py

class Order:
    def __init__(self, order_id, product_list):
        self.order_id = order_id
        self.product_list = product_list

    def __repr__(self):
        return f"Order(order_id={self.order_id}, product_list={self.product_list})"

class OrderProcessor:
    def __init__(self):
        self.orders = []

    def create_order(self, order):
        self.orders.append(order)

    def get_orders(self):
        return self.orders
