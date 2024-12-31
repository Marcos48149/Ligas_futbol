import snowflake.connector

try:
    conn = snowflake.connector.connect(
        user="",
        password="",
        account="",
        warehouse="",
        database="new",
        schema="public",
        role="accountadmin"
    )
    print("Conexión exitosa:", conn.cursor().execute("SELECT CURRENT_VERSION()").fetchone())
except Exception as e:
    print("Error en la conexión:", str(e))
