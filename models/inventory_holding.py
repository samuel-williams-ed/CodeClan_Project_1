class Inventory_holding():
    def __init__(self, 
    input_display_name, 
    input_number_in_stock, 
    input_retail_price, 
    input_product_object,
    _id=None):
        self.display_name = input_display_name
        self.number_in_stock = input_number_in_stock
        self.retail_price = input_retail_price
        self.product = input_product_object
        self.id = _id

