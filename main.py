# Note: the module name is psycopg, not psycopg3
import psycopg

# Connect to an existing database
with psycopg.connect(dbname="MarvelTradingCards",
                     user="",
                     password="",
                     host="localhost",
                     port="5432") as conn:
# psycopg.connect("dbname=MarvelTradingCards user=postgres")

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM marvel_beginnings_vol2_series2")
        cur.fetchone()

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        for record in cur:
            print(record)