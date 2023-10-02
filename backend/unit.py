
def get_unit(cnx):
    cursor = cnx.cursor()
    query = "select * from unit"
    cursor.execute(query)
    response = []
    for (unit_id, unit_name) in cursor:
        response.append({
            'unit_id': unit_id,
            'unit_name': unit_name
        })
    return response


if __name__ == '__main__':
    from sql_connection import get_connection

    cnx = get_connection()
    # print(get_all_products(connection))
    print(get_unit(cnx))