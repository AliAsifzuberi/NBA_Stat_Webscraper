import pandas as pd
import requests
pd.set_option('display.max_columns', None)
import time
import numpy as np
welcome = "WELCOME TO NBA STAT WEBSCRAPER PROJECT"

for char in welcome:
    print("-")

print("WELCOME TO NBA STAT WEBSCRAPER PROJECT")

year  = input("Enter a year in the format yyyy-yy: ")
seasonType = (input("Enter Season Type: "))
statCat = (input("Enter Stat Type: "))

url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season='+year+'&SeasonType='+seasonType+'&StatCategory='+statCat+''

r = requests.get(url=url).json()

table_headers = r['resultSet']['headers']
print(pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers))


