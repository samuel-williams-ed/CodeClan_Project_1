from models.product import Product
from models.inventory_holding import Inventory_holding
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manu_rep
import repositories.product_repository as prod_rep
import repositories.inventory_repository as invent_rep

########################## Load & Save Test Objects ############################

#load test Manufacturers
test_manufacturer_1 = Manufacturer("test", "Testing", 3.00)
test_manufacturer_2 = Manufacturer("Smithies", "1/15 Underground, Cavern Street.", 17)

# have to save these before passing them into the test_products
# save manufacturer test_objects
# print(" (console) ")
test_manufacturer_1 = manu_rep.save(test_manufacturer_1)
test_manufacturer_2 = manu_rep.save(test_manufacturer_2)
# print(f"manu._id = {test_manufacturer_1._id}")
# print(f"manu._id = {test_manufacturer_2._id}")
test_manufacturer_list = [test_manufacturer_1, test_manufacturer_2]

#load test Products
test_product_1 = Product("Pickaxe",
"A basic pickaxe, used to mine for ore and break up tough ground.",
"Model X: Picker", "hand-weapon", 2, test_manufacturer_1, True, 3)
test_product_2 = Product("Sword", 
"A standard issue short sword. Used for stabbing, slashing, and general purpose swording.",
"SND03-27-B", "util", 2, test_manufacturer_2, True, 4)
test_product_list = [test_product_1, test_product_2]

#save test products
test_product_1 = prod_rep.save(test_product_1)
test_product_2 = prod_rep.save(test_product_2)
#print(f"console: test_prod_1: \n{test_product_1.__dict__}")
# print(f"console: test_prod_2: \n{test_product_2.__dict__}")

#load test Inventory_holdings
test_inventory_item_1 = Inventory_holding(
    "Basics Range Pick-axe", 8, 8, test_product_1)
test_inventory_item_2 = Inventory_holding(
    "Basics Range Short Sword", 20, 6, test_product_2)
test_inventory_list = [test_inventory_item_1, test_inventory_item_2]

# save inventory items
test_inventory_item_1 = invent_rep.save(test_inventory_item_1)
test_inventory_item_2 = invent_rep.save(test_inventory_item_2)
test_inventory_list = [test_inventory_item_1, test_inventory_item_2]

####################### repository functions ############################








####################### test functions ############################

def get_inventory():
    return test_inventory_list

########################## Printing ############################
# general purpose method to print all lists
def print_list(list):
    for item in list:
        print("")
        print(item.__dict__)

# print_list(test_product_list)
# print_list(test_manufacturer_list)
print_list(test_inventory_list)
