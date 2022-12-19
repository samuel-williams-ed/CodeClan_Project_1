-- write your tables in here. 

-- granchild
DROP TABLE IF EXISTS inventory;
--  child
DROP TABLE IF EXISTS products;
-- parent
DROP TABLE IF EXISTS suppliers;


-- album (child) inherits artists (parent)
-- or the child has no genes to inherit

-- CREATE TABLE suppliers (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255)
-- );

CREATE TABLE suppliers(
    id SERIAL PRIMARY KEY
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    model VARCHAR(255),
    type VARCHAR(255),
    combat_strength INT,
    manufacturer_object_id INT,
    taking_orders INT,
    wholesale_cost INT,
    supplier_id INT
);
-- supplier_id INT NOT NULL REFERENCES suppliers(id)

CREATE TABLE inventory(
    id SERIAL PRIMARY KEY,
    display_name VARCHAR(255),
    number_in_stock INT,
    retail_price INT,
    product_object_id INT
);

