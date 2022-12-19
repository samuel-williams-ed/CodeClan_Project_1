from db.run_sql import run_sql

from models.manufacturer import Manufacturer

    #value passed in SQL db for manufacturer and supplier is the id only
    #when we pull data dfrom db we use id
    #to create and return an instance of manufacturer that is within this instance of product


def save(manufacturer_object):
    # print(f"Debug: testing save(): product.name = {manufacturer_object.name} || id = {manufacturer_object._id}")
    sql = "INSERT INTO suppliers (name, address, delivery_fee) VALUES (%s, %s, %s) RETURNING *"
    values = [manufacturer_object.name,
    manufacturer_object.address,
    manufacturer_object.delivery_fee]

    # print("")
    # print(f"Debug: manufacturer_object _id = {manufacturer_object._id}")   

    # print("")
    # print(f"Debug: values = {values}")    
    
    query_results = run_sql(sql, values)

    # print("")
    # print(f"Debug: query result = {query_results}")   

    query_result = query_results[0]
    manufacturer_id = query_result['id']
    result = Manufacturer(query_result['name'], query_result['address'], query_result['delivery_fee'], query_result['id'])

    return result


def get_by_id(input_id):
    