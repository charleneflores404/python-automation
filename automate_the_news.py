from selenium import webdriver

web = 'https://www.thesun.co.uk/sport/football/'

# Creating the driver
driver = webdriver.Chrome()
driver.get(web)
