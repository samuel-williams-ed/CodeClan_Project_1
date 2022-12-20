from db.run_sql import run_sql
import repositories.product_repository as prod_repo
from models.inventory_holding import Inventory_holding



def save(input_inventory_object):
    sql = "INSERT INTO inventory (display_name, number_in_stock, retail_price, product_object_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [
        input_inventory_object.display_name,
        input_inventory_object.number_in_stock,
        input_inventory_object.retail_price,
        input_inventory_object.product._id]
    query_results = run_sql(sql, values)
    query_result = query_results[0]

    ### return product with SQL db id ###
    product_id = query_result['product_object_id']
    product_object = prod_repo.get_by_id(product_id)

    #TODO build inventory instance:
    result = Inventory_holding(query_result['display_name'],
    query_result['number_in_stock'],
    query_result['retail_price'],
    product_object,
    query_result['id'])
    return result

def select_all():
    sql = "SELECT * FROM inventory"
    query_results = run_sql(sql)
    return_list = []
    for query_result in query_results:
        # get instance of product
        product_id = query_result['product_object_id']
        product_object = prod_repo.get_by_id(product_id)
        #build instance of Inventory
        found_instance = Inventory_holding(query_result['display_name'],
            query_result['number_in_stock'],
            query_result['retail_price'],
            product_object,
            query_result['id'])
        return_list.append(found_instance)
    return return_list

def get_by_id(input_id):
    sql = "SELECT * FROM inventory WHERE id=%s"
    values = [input_id]
    query_results = run_sql(sql, values)
    query_result = query_results[0]

    product_id = query_result['product_object_id']
    product_object = prod_repo.get_by_id(product_id)

    result = Inventory_holding(query_result['display_name'],
    query_result['number_in_stock'],
    query_result['retail_price'],
    product_object,
    query_result['id'])
    return result


