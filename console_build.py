from models.product import Product
from models.inventory_holding import Inventory_holding
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manu_rep
import repositories.product_repository as prod_rep
import repositories.inventory_repository as invent_rep

########################## Load & Save Test Objects ############################
print("\n############## console.build.py ####################\n")
test_manufacturer_list = []
test_product_list = []
test_inventory_list = []

def load_and_save_test_data():

    #load test Manufacturers
    print("Building & saving Manufacturers\n")
    test_manufacturer_1 = Manufacturer("test", "Testing", 3.00)
    test_manufacturer_2 = Manufacturer("Smithies", "1/15 Underground, Cavern Street.", 17)
    # save test Manufacturers
    test_manufacturer_1 = manu_rep.save(test_manufacturer_1)
    test_manufacturer_2 = manu_rep.save(test_manufacturer_2)
    test_manufacturer_list.append([test_manufacturer_1, test_manufacturer_2])
    #load test Products
    print("Building & saving Products\n")
    test_product_1 = Product("Pickaxe",
    "A basic pickaxe, used to mine for ore and break up tough ground.", "Model X: Picker", "hand-weapon", 2, test_manufacturer_1, True, 3)
    test_product_2 = Product("Sword", 
    "A standard issue short sword. Used for stabbing, slashing, and general purpose swording.","SND03-27-B", "util", 2, test_manufacturer_2, True, 4)
    #save test products
    test_product_1 = prod_rep.save(test_product_1)
    test_product_2 = prod_rep.save(test_product_2)
    test_product_list.append([test_product_1, test_product_2])
    #load test Inventory_holdings
    print("Building & saving Inventory_holdings\n")
    test_inventory_item_1 = Inventory_holding("Basics Range Pick-axe", 8, 8, test_product_1)
    test_inventory_item_2 = Inventory_holding("Basics Range Short Sword", 20, 6, test_product_2)
    # save inventory items
    test_inventory_item_1 = invent_rep.save(test_inventory_item_1)
    test_inventory_item_2 = invent_rep.save(test_inventory_item_2)
    test_inventory_list.append([test_inventory_item_1, test_inventory_item_2])

####################### test functions ############################

def get_inventory():
    return test_inventory_list

def get_inventory_list_length():
    return len(test_inventory_list)

########################## Printing ############################
# general purpose method to print all lists
def print_list(list):
    for item in list:
        print("")
        print(item.__dict__)

# print("\nBuilding test")
# print("\ntest_product_list:")
# print_list(test_product_list)
# print("\ntest_manufacturer_list:")
# print_list(test_manufacturer_list)
# print("\ntest_inventory_list:")
# print_list(test_inventory_list)
