from db.run_sql import run_sql

from models.product import Product
import repositories.manufacturer_repository as manu_rep

    #value passed in SQL db for manufacturer and supplier is the id only
    #when we pull data dfrom db we use id
    #to create and return an instance of manufacturer that is within this instance of product


#     id SERIAL PRIMARY KEY,
#     name VARCHAR(255),
#     description VARCHAR(255),
#     model VARCHAR(255),
#     type VARCHAR(255),
#     combat_strength INT,
#     manufacturer_object_id INT,
#     taking_orders INT,
#     wholesale_cost INT,
#     supplier_id INT NOT NULL REFERENCES suppliers(id)

def save(product):

    # print("")
    # print("saving product: ")

    # print("")
    # print(f"Debug: product_repo: save(): \nproduct.name = {product.name} || id = {product._id} \nProduct_manufacturer_id = {product.manufacturer._id}")

    sql = "INSERT INTO products (name, description, model, type, combat_strength, manufacturer_object_id, taking_orders, wholesale_cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"

    values = [product.name,
        product.description,
        product.model,
        product.type,
        product.combat_strength,
        product.manufacturer._id,
        product.taking_orders,
        product.wholesale_cost]

    # print("")
    # print(f"Debug: product_repo: \nmanufacturer_object _id = {product.manufacturer._id}")   

    # print("")
    # print(f"Debug: product_repo: values = \n{values}")    
    
    query_results = run_sql(sql, values)
    query_result = query_results[0]

    # print("")
    # print(f"Debug: product_repo: query result = {query_results}")   

    ### return product with SQL db id ###

    # take first returned object
    # query_result = query_results[0]
    # TODO get id value
    manufacturer_id = query_result['manufacturer_object_id']

    # TODO build manufacturer instance from SQL data
    manu_rep.get_by_id(manufacturer_id)

    #TODO build product instance:
    result = Product(query_result['name'],
    query_result['description'],
    query_result['model'],
    query_result['type'],
    query_result['combat_strength'],
    manufacturer_id,
    query_result['taking_orders'],
    query_result['wholesale_cost'],
    query_result['id'])

    # TODO attach manufacturer_object to product being returned

    return result




# def select_album(album_id):
#     album = None

#     sql = " SELECT * FROM albums WHERE id=%s"
#     values = [album_id]
    
#     #single album where matches album_id
#     results = run_sql(sql, values)
    
#     if results:
#         result = results[0]
#         artist = rep_rep.select_single(result['artist_id'])
#         album = Album(result['title'], result['genre'], artist, result['id'])
#     return album

def select_all_products():
    sql = " SELECT * FROM products"
    return run_sql(sql)

