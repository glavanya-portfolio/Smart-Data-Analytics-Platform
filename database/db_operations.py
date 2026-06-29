from database.db_connection import create_connection


def save_to_mysql(df, table_name):

    connection = create_connection()

    cursor = connection.cursor()

    columns = []

    for column in df.columns:
        columns.append(f"`{column}` TEXT")

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name}(
        id INT AUTO_INCREMENT PRIMARY KEY,
        {",".join(columns)}
    )
    """

    cursor.execute(create_table_query)

    cursor.execute(f"DELETE FROM {table_name}")

    placeholders = ",".join(["%s"] * len(df.columns))

    insert_query = f"""
    INSERT INTO {table_name}
    ({",".join([f"`{c}`" for c in df.columns])})
    VALUES ({placeholders})
    """

    for row in df.astype(str).values.tolist():
        cursor.execute(insert_query, row)

    connection.commit()

    cursor.close()

    connection.close()