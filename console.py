from models.product import Product
from models.inventory_holding import Inventory_holding
from models.manufacturer import Manufacturer

from console_build import test_product_list, test_inventory_list, test_manufacturer_list

import repositories.manufacturer_repository as manu_rep
import repositories.product_repository as prod_rep

####################### test functions ############################



def check_data():
    print("\ntest_product_list:")
    print_list(test_product_list)
    print("\ntest_manufacturer_list:")
    print_list(test_manufacturer_list)
    print("\ntest_inventory_list:")
    print_list(test_inventory_list)
    return None

########################## Printing ############################
# general purpose method to print all lists
def print_list(list):
    for item in list:
        print("")
        print(item.__dict__)

# check_data()