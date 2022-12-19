from flask import render_template, redirect
from flask import Blueprint

from console import get_inventory as get_inventory_list
from models.inventory_holding import Inventory_holding
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
    return render_template("/shop/inventory_display_block.html")

