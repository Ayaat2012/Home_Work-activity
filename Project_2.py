import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)
print("Opened database successfully.")

#Loading the 'Match' table
matches = pd.read_sql("""SELECT * FROM Matches;""", conn)
print("\nMatches Table (first 5 rows):")
print(matches.head())

#Checking details of all matches won by Mumbai Indians
#(Assuming Mumbai Indians has Team_Id = 7)
MI_wins = pd.read_sql("""SELECT * FROM Match
                      WHERE Match_Winner == 7;""", conn)
print("\n--- All MI Wins ---")
print(MI_wins)

#Matches won by MI in last two seasons
#(Assuming seasons 8 and 9)
MI_S8_S9 = pd.read_sql("""SELECT * FROM Match
                       WHERE Match_Winner == 7 AND Season_Id IN (8,9);""", conn)
print("\n--- MI Wins in Seasons 8 & 9 ---")
print(MI_S8_S9)

#Finding new teams(team names starting with 'De')
new_teams = pd.read_sql("""SELECT * FROM Team
                        WHERE Team_Name LIKE 'De%';""", conn)
print("\n--- New Teams (Name starts with 'De') ---")
print(new_teams)

#Minimum & Maximum winning margin
min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin) AS Min_Margin,
                             MAX(Win_Margin) AS Max_Margin
                             FROM Match;""", conn)
print("\n--- Minimum & Maximum Winning Margin ---")
print(min_max_margin)