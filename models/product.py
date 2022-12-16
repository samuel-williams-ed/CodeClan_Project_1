class Product():
    def __init__(self,
    input_name,
    input_description,
    input_model,
    input_type,
    input_combat_strength,
    input_magical_bool,
    id=None):
        self.name = input_name
        self.descritpion = input_description
        self.model = input_model
        self.type = input_type
        self.combat_strength = input_combat_strength
        self.magical = input_magical_bool
        self._id = id


# class Product():
#  - name
#  - description
#  - model
#  - type (Armour, hand-weapon, ranged_weapon, magical_weapon, util)
#  - combat_strength
#  - magical_item (boolean)
#  - Manufacturer (object)
#  - id