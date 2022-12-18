from flask import render_template, redirect
from flask import Blueprint

from console import get_inventory as get_inventory_list
from models.inventory_holding import Inventory_holding
# import repositories.book_repository as book_repository
# import repositories.author_repository as author_repository

shop_blueprint = Blueprint("shops", __name__)

@shop_blueprint.route("/")
def tasks():
    inventory_list = get_inventory_list()
    return render_template("/index.html", inventory_list=inventory_list)

