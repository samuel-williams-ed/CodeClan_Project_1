class Product():
    def __init__(self,
    input_name,
    input_description,
    input_model,
    input_type,
    input_combat_strength,
    input_manufacturer_object,
    input_taking_orders,
    input_wholesale_cost,
    _id=None):
        self.name = input_name
        self.description = input_description
        self.model = input_model
        self.type = input_type
        self.combat_strength = input_combat_strength
        self.manufacturer = input_manufacturer_object
        self.taking_orders = input_taking_orders
        self.wholesale_cost = input_wholesale_cost
        self._id = _id
        print("\nProduct: a new product has been made\n")
