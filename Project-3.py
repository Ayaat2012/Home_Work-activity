import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)


table = pd.read_sql("""SELECT * FROM sqlite_master
                    WHERE type = 'table';""", conn)
print(table)

matches = pd.read_sql("""SELECT * FROM match;""", conn)
print(matches)

#Getting the Average win margin of all the winning teams of season 9
result1 = pd.read_sql("""
                    SELECT AVG(Win_Margin) AS avg_margin, Match_Winner
                    FROM match
                    WHERE Season_Id = 9
                    GROUP BY Match_Winner
                    ORDER BY AVG(Win_Margin);
""", conn)
print(result1)

#Get the Min, Max and Average Win Margins
#Also get the total number of players who recieved Man of The Match awards
result2 = pd.read_sql("""
  SELECT MIN(Win_Margin) AS min_margin
         MAX(Win_Margin) AS max_margin
         AVG(Win_Margin) AS average_margin
         COUNT(Win_Margin) AS unique_mom_players
    FROM Match
""", conn)
print(result2)

#Return the total win_margins for all the winners in season 9
result3 = pd.read_sql("""
    SELECT SUM(Win_Margin) AS total_win_margin
    FROM match
    WHERE Season_Id = 9;
""", conn)
print(result3)