from flask import render_template, redirect
from flask import Blueprint

from console_build import get_inventory as get_inventory_list, get_inventory_list_length
from models.inventory_holding import Inventory_holding
import repositories.product_repository as prod_rep
# import repositories.book_repository as book_repository
# import repositories.author_repository as author_repository

shop_blueprint = Blueprint("shops", __name__)

@shop_blueprint.route("/example")
def example():
    inventory_list = get_inventory_list()
    return render_template("/example.html", inventory_list=inventory_list)

@shop_blueprint.route("/")
def home():
    return render_template("/home.html")

@shop_blueprint.route('/shop/about')
def index_about():
    return render_template("/shop/about.html")

@shop_blueprint.route('/shop/gear')
def index_gear():
    return render_template("/shop/gear.html")

@shop_blueprint.route('/shop/suppliers')
def index_suppliers():
    product_list = prod_rep.select_all_products()
    print(f"\n debug: inventory_console: \nindex_suppliers: product_list: \n{product_list}")
    print(f"debug: length of list: {get_inventory_list_length()}")
    return render_template("/shop/inventory_display_block.html", product_list=product_list)

