from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

web = 'https://www.thesun.co.uk/sport/football/'


# Set up Chrome in headless mode (run in the background without launching the driver)
options = Options()
options.add_argument("--headless=new")


# Creating the driver

driver = webdriver.Chrome(options=options)
driver.get(web)


# Finding Elements

# explore the browser Inspect tab and find the right elements
# use xpath; can also use classname, id, or other attributes
containers = driver.find_elements(by='xpath', value='//div[@class="story__copy-container"]')

titles = []
subtitles = []
links = []

# driver.find_element(by='xpath', value='//div[@class="story__copy-container"]/a/p')
for container in containers:
    title = container.find_element(by='xpath', value='./a/p').text
    subtitle = container.find_element(by='xpath', value='./a/h3').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


# Exporting data to a CSV file

headlines_dict = {'title': titles, 'subtitle': subtitles, 'link': links }
df_headlines = pd.DataFrame(headlines_dict)
df_headlines.to_csv('headline-headless.csv')

driver.quit()