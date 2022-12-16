from models.product import Product
from models.inventory_holding import Inventory_holding

########################## Load Test Objects ############################
#load test Products

test_product_1 = Product("Pickaxe",
"A basic pickaxe, used to mine for ore and break up tough ground.",
"Model X: Picker", "hand-weapon", 2, False)
test_product_2 = Product("Sword", 
"A standard issue short sword. Used for stabbing, slashing, and general purpose swording.",
"SND03-27-B", "hand-weapon", 2, False)
test_product_list = [test_product_1, test_product_2]

#load test Manufacturers
test_manufacturer_1 = {"test":"test"}
test_manufacturer_2 = {"test":"test"}
test_manufacturer_list = [test_manufacturer_1, test_manufacturer_2]

#load test Inventory_holdings
test_inventory_item_1 = Inventory_holding(
    "Basics Range Pick-axe", 8, 8, test_product_1, test_manufacturer_1)
test_inventory_item_2 = Inventory_holding(
    "Basics Range Short Sword", 20, 6, test_product_2, test_manufacturer_2)
test_inventory_list = [test_inventory_item_1, test_inventory_item_2]





########################## Printing ############################
# general purpose method to print all lists
def print_list(list):
    for item in list:
        print("")
        print(item.__dict__)

print_list(test_product_list)
# print_list(test_manufacturer_list)
print_list(test_inventory_list)
