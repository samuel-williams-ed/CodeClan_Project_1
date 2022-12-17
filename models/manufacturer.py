class Manufacturer():
    def __init__(self,
    input_name,
    input_address,
    input_delivery_fee,
    _id=None):
        self.name = input_name
        self.address = input_address
        self.delivery_fee = input_delivery_fee
        self._id = _id
