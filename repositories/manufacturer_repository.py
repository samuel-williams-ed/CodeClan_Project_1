from db.run_sql import run_sql

from models.manufacturer import Manufacturer

    #value passed in SQL db for manufacturer and supplier is the id only
    #when we pull data dfrom db we use id
    #to create and return an instance of manufacturer that is within this instance of product


def save(manufacturer_object):
    # print(f"Debug: testing save(): product.name = {manufacturer_object.name} || id = {manufacturer_object._id}")
    sql = "INSERT INTO suppliers (name, address, delivery_fee) VALUES (%s, %s, %s) RETURNING *"
    values = [
        manufacturer_object.name,
        manufacturer_object.address,
        manufacturer_object.delivery_fee]
    query_results = run_sql(sql, values)
    query_result = query_results[0]
    result = Manufacturer(query_result['name'], query_result['address'], query_result['delivery_fee'], query_result['id'])
    return result


def get_by_id(input_id):
    sql = "SELECT * FROM suppliers WHERE id=%s"
    values = [input_id]
    query_results = run_sql(sql, values)
    query = query_results[0]
    # print(f"debug: manu_repo.get_by_id: query = \n{query}")
    return Manufacturer(query['name'], query['address'], query['delivery_fee'], query['id'])
    # print(f"debug: manu_rep.get_by_id: n\{result.__dict__}")
    # return result

