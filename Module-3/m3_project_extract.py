# Date: 25.11.2022
# Descrption: this file connects to a sqlite database and extracts the necessary data for further analysis

# Datasource: https://www.kaggle.com/datasets/hugomathien/soccer

# import required packages

import sqlite3
import os
import pandas as pd
from google.colab import drive

# set Pandas options
pd.set_option('max_columns', None)
pd.set_option('display.max_columns', None)

# connect to Google Drive
drive.mount('content/')

# connect to sqlite database
# CHANGE the path if required

con = sqlite3.connect("content/MyDrive/Projekt/M3/database.sqlite")
cur = con.cursor()

# overvriew database.sqlite tables

# Country
# League
# Match
# Player
# Player_Attributes
# Team
# Team_Attributes

# set SQL query to extract data
cur.execute(
    '''SELECT
        Match.id,
        Match.date,
        Match.season,
        Match.stage,
        Match.country_id,
        Country.name AS Country_Name,
        Match.league_id,
        League.name AS League_Name,
        Match.home_team_api_id,
        HT.team_long_name AS HT_long_name,
        Match.away_team_api_id,
        AT.team_long_name AS AT_long_name,
        home_team_goal,
        away_team_goal,
        home_player_1,
        home_player_2,
        home_player_3,
        home_player_4,
        home_player_5,
        home_player_6,
        home_player_7,
        home_player_8,
        home_player_9,
        home_player_10,
        home_player_11,
        away_player_1,
        away_player_2,
        away_player_3,
        away_player_4,
        away_player_5,
        away_player_6,
        away_player_7,
        away_player_8,
        away_player_9,
        away_player_10,
        away_player_11,
        goal,
        shoton,
        shotoff,
        foulcommit,
        card,
        cross,
        corner,
        possession
    from Match
    LEFT JOIN Country ON Match.country_id = Country.id
    LEFT JOIN League ON Match.league_id = League.id
    LEFT JOIN Team AS HT on HT.team_api_id = Match.home_team_api_id
    LEFT JOIN Team AS AT on AT.team_api_id = Match.away_team_api_id
    WHERE 1 = 1
    AND Country.Name = "Italy"
    AND Match.season = "2015/2016"'''

)

# execute query
rows = cur.fetchall()

# extract column names and convert to pandas dataframe
names = list(map(lambda x: x[0], cur.description))
df  = pd.DataFrame(rows, columns = names)
