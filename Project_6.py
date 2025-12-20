# Import necessary libraries
import pandas as pd
import numpy as np
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)

table = pd.read_sql("""
                SELECT * 
                FROM sqlite_master
                WHERE type = 'table';""", conn)
print(table)


# Fetching details of all matches played by CSK in year 2015
csk_matches = pd.read_sql("""
                            SELECT Match_Id, Team_2 AS Away_Team, Toss_Winner, Match_Winner
                            FROM Match
                            WHERE Team_1 =
                            (SELECT Team_1
                            FROM Match
                            WHERE Team_! == 3 AND Season_Id == 8);
""", conn)
print(csk_matches)


# Fetching details of all matches won by CSK in year 2015 
csk_wins = pd.read_sql("""
                    SELECT Match_Id, Runs_Scored AS Total_Runs, Innings_No
                    FROM Batsman_Scored
                    WHERE Total_Runs > 5 AND Match_Id IN
                    (SELECT Match_Id
                    FROM Match
                    WHERE Season_Id == 8);
""", conn)
print(csk_wins)


# Fetching details of all the matches where batsman scores more than 5 in year 2015 
match_runs = pd.read_sql("""
                        SELECT MaTCH_Id, Runs_Scored AS Total_Runs, Innings_No
                        FROM Batsman_Scored
                        WHERE Total_Runs > 5 AND Match_Id IN
                        (SELECT Match_Id
                        FROM Match
                        WHERE Season_Id == 8);
""", conn)
print(match_runs)


# Fetching details of matches played in year 2015 where Total Runs Scored were greater than average scored run
avg_runs = pd.read_sql("""
                    SELECT Match_Id, Runs_Scored AS Total_Runs, Innings_No
                    FROM Batsman_Scored
                    WHERE Innings_No == 1 AND Runs_Scored >
                    (SELECT AVG(Runs_Scored)
                    FROM Batsman_Scored);
""", conn)
print("\nMatches with Scored  Runs Greater Than Average Scored Runs(Query from first image)")
print(avg_runs)