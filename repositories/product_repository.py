from db.run_sql import run_sql

from models.product import Product
import repositories.manufacturer_repository as manu_rep

def save(product):
    sql = "INSERT INTO products (name, description, model, type, combat_strength, manufacturer_object_id, taking_orders, wholesale_cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name,
        product.description,
        product.model,
        product.type,
        product.combat_strength,
        product.manufacturer._id,
        product.taking_orders,
        product.wholesale_cost]
    query_results = run_sql(sql, values)
    query_result = query_results[0] 

    # return Manufacturer object frin SQL db using id ###
    manufacturer_id = query_result['manufacturer_object_id']
    manufacturer_object = manu_rep.get_by_id(manufacturer_id)

    # build Product instance:
    result = Product(query_result['name'],
    query_result['description'],
    query_result['model'],
    query_result['type'],
    query_result['combat_strength'],
    manufacturer_object,
    query_result['taking_orders'],
    query_result['wholesale_cost'],
    query_result['id'])
    print("product_repo: saved a new Product\n")
    return result

def select_all_products():
    sql = " SELECT * FROM products"
    return run_sql(sql)

def get_by_id(product_object_id):
    sql = "SELECT * FROM products WHERE id=%s"
    values = [product_object_id]
    query_results = run_sql(sql, values)
    query = query_results[0]
    manufacturer_object = manu_rep.get_by_id(query['manufacturer_object_id'])

    return Product(query['name'], query['description'], query['model'], query['type'], query['combat_strength'],
    manufacturer_object, query['taking_orders'], query['wholesale_cost'], query['id'])
