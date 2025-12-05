import pandas as pd
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print("Opened data successfully.")


#Read sql query for getting all the tables of database into dataform
table = pd.read_sql("""SELECT * FROM sqlite_master
                    WHERE type = 'table';""", conn)

print(table)