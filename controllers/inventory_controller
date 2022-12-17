from flask import render_template, redirect
from flask import Blueprint

from models.inventory_holding import Inventory_holding
# import repositories.book_repository as book_repository
# import repositories.author_repository as author_repository

shop_blueprint = Blueprint("books", __name__)

@shop_blueprint.route("/shop")
def tasks():
    # books = book_repository.select_all()
    return render_template("/shop/index.html")

# @books_blueprint.route("/books/<id>/delete", methods=["POST"])
# def destroy(id):
#     book_repository.delete(int(id))
#     return redirect("/books")