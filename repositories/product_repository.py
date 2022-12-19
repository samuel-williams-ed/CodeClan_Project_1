from db.run_sql import run_sql

from models.product import Product

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

    print(f"Debug: testing save(): product.name = {product.name} || id = {product._id}")

    sql = "INSERT INTO products (name, description, model, type, combat_strength, manufacturer_object_id, taking_orders, wholesale_cost) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"

    values = [product.name, product.description, product.model, product.type, product.combat_strength, product.manufacturer._id, product.taking_orders, product.wholesale_cost]

    print("")
    print(f"Debug: values = {values}")    
    
    query_results = run_sql(sql, values)

    print("")
    print(f"Debug: query result = {query_results}")   

    ### return product with SQL db id ###

    # take first returned object
    # query_result = query_results[0]
    # TODO get id value

    # TODO build manufacturer instance from SQL data

    # TODO attach manufacturer_object to product being returned

    return query_results




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

