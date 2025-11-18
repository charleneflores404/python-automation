# Extract CSV from website
# Read a .csv from a URL with Pandas
# Target website: https://www.football-data.co.uk/data.php

import pandas as pd
import requests
from io import StringIO # to make the text behave like a file

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# reading 1 csv file from the website
url2 = 'https://www.football-data.co.uk/mmz4281/2526/E0.csv'
response = requests.get(url2, headers=headers)
df_premier25 = pd.read_csv(StringIO(response.text))
# showing dataframe
print(df_premier25)

# renaming columns
df_premier25.rename(columns={'FTHG':'home_goals', 
                             'FTAG':'away_goals'}, inplace=True)
# show dataframe
print(df_premier25)