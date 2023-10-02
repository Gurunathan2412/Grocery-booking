from sql_connection import get_connection


def get_all_product(cnx):

    cursor = cnx.cursor()
    query = "SELECT products.product_id, products.name, products.unit_id, products.price_per_unit, unit.unit_name\
    FROM grocery.products inner join grocery.unit on products.unit_id=unit.unit_id"
    cursor.execute(query)

    respond = []
    for (product_id, name, unit_id, price, unit_name) in cursor:
        respond.append(
            {
                "product_id": product_id,
                "name": name,
                "unit_id": unit_id,
                "price_per_unit": price,
                "unit_name": unit_name
            }
        )
        # print(product_id, name, unit_id, price, unit_name)
    cnx.close()
    return respond


def add_product(cnx, product):
    cursor = cnx.cursor()
    query = "INSERT INTO grocery.products (name, unit_id, price_per_unit) VALUES (%s, %s, %s);"
    print(product)
    data = (product["name"], product["unit_id"], product["price_per_unit"])
    cursor.execute(query, data)
    cnx.commit()
    return cursor.lastrowid


def delete_product(cnx, product_id):
    cursor = cnx.cursor()
    query = "DELETE FROM products where product_id="+str(product_id)
    cursor.execute(query)
    cnx.commit()
    return cursor.lastrowid


if __name__ == "__main__":
    cnx = get_connection()
    # print(delete_product(cnx, 13))
