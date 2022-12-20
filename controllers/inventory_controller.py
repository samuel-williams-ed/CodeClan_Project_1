from flask import render_template, redirect, request
from flask import Blueprint

from console_build import get_inventory, get_inventory_list_length
from models.inventory_holding import Inventory_holding
import repositories.inventory_repository as invent_rep
import repositories.product_repository as prod_rep
import repositories.manufacturer_repository as manu_rep

shop_blueprint = Blueprint("shops", __name__)

@shop_blueprint.route("/example")
def example():
    inventory_list = get_inventory() #list
    return render_template("/example.html", inventory_list=inventory_list)

@shop_blueprint.route("/")
def home():
    return render_template("/home.html")

@shop_blueprint.route('/shop/about')
def index_about():
    return render_template("/shop/about.html")

@shop_blueprint.route('/shop/gear')
def index_gear():
    inventory_list = invent_rep.select_all()
    return render_template("/shop/gear.html", inventory_list=inventory_list )

@shop_blueprint.route('/shop/suppliers')
def index_suppliers():
    product_list = prod_rep.select_all_products()
    # art assets only allow for 10 to display at a time
    # remove any extra
    # TODO build a scroll into the html element that displays the list
    cleaned_product_list = product_list
    if len(product_list) > 10:
        cleaned_product_list.clear()
        for product in product_list:
            if cleaned_product_list < 10:
                cleaned_product_list.append(product)
            else:
                break
    # print(f"\n debug: inventory_console: \nindex_suppliers: product_list: \n{product_list}")
    # print(f"debug: length of list: {get_inventory_list_length()}")
    return render_template("/shop/supplier_display_block.html", product_list=cleaned_product_list)

@shop_blueprint.route('/shop/supplier/inventory/<inventory_id>', methods=["POST"])
def show_suppliers(inventory_id):
    inventory_object = invent_rep.get_by_id(int(inventory_id))
    return render_template("shop/supplier_display_block.html", inventory_object=inventory_object)