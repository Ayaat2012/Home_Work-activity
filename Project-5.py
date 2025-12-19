# Import necessary libraries
import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)
print("Opened data successfully.")

tables = pd.read_sql("""
                    SELECT * 
                    FROM sqlite_master
                    WHERE type = 'table';""", conn)
print(tables)


#INNER JOIN
inner_join = pd.read_sql("""
                        SELECT c.Country_Id, c.Country_Name, ci.City_Name
                        FROM country c
                        INNER JOIN city ci
                        ON c.Country_Id = ci.Country_Id;""", conn)
print(inner_join)

#LEFT OUTER JOIN
left_join = pd.read_sql("""
                        SELECT *
                        FROM player
                        LEFT JOIN season
                        ON player.Player_Id = season.Man_of_the_Series;""", conn)
print(left_join)


#CROSS JOIN
cross_join = pd.read_sql("""
                        SELECT c.Country_Id, c.Country_Name, ci.City_Name
                        FROM country c
                        CROSS JOIN city ci;""", conn)
print(cross_join)

#UNION
union = pd.read_sql("""
                SELECT Player_Name
                FROM player
                UNION
                SELECT Team_Name
                FROM team;""", conn)
print(union)