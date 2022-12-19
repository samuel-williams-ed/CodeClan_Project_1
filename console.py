from models.product import Product
from models.inventory_holding import Inventory_holding
from models.manufacturer import Manufacturer

from console_build import test_product_list, test_inventory_list, test_manufacturer_list

import repositories.manufacturer_repository as manu_rep
import repositories.product_repository as prod_rep

from console_build import load_and_save_test_data as build_test_data

####################### test functions ############################
print("\n############## console.py ####################\n")

# general purpose method to print all lists
def print_list(list):
    for item in list:
        print("")
        print(item.__dict__)

def check_data():
    print("\ntest_product_list:")
    print_list(test_product_list)
    print("\ntest_manufacturer_list:")
    print_list(test_manufacturer_list)
    print("\ntest_inventory_list:")
    print_list(test_inventory_list)
    return None

build_test_data()
check_data()