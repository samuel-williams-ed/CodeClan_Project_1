from models.product import Product

#load test products
test_product_1 = Product("Pickaxe",
"A basic pickaxe, used to mine for ore and break up tough ground.",
False, "hand-weapon", 2)

test_product_2 = Product("Sword", 
"A standard issue short sword. Used for stabbing, slashing, and general purpose swording.",
False, "hand-weapon", 2)

test_product_list = [test_product_1, test_product_2]

# test print all test items
def print_list(list):
    for item in list:
        print("")
        print(item.__dict__)

print_list(test_product_list)

