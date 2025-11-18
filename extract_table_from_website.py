import pandas as pd
import requests
from io import StringIO # to make the text behave like a file

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

url1 = "https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)"

response = requests.get(url1, headers=headers)
simpsons = pd.read_html(response.text) # a list of tables from a website

print(len(simpsons))
print(simpsons[1])