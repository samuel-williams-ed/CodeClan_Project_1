class Manufacturer():
    def __init__(self, input_name, input_wholesale_price, input_delivery_fee, input_taking_orders, input_id=None):
        self.name = input_name
        self.wholesale_price = input_wholesale_price
        self.delivery_fee = input_delivery_fee
        self.taking_orders = input_taking_orders
        self._id = input_id


#  - manufacturer_name
#  - wholesale_cost
#  - delivery_fee
#  - taking_orders (bool) (extension)
#  - id 