from models.product import Product
from models.inventory_holding import Inventory_holding
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manu_rep
import repositories.product_repository as prod_rep

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
# print_list(test_inventory_list)