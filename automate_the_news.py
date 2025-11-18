from selenium import webdriver

web = 'https://www.thesun.co.uk/sport/football/'

# Creating the driver

driver = webdriver.Chrome()
driver.get(web)

# Finding Elements

# explore the browser Inspect tab and find the right elements
# use xpath; can also use classname, id, or other attributes
containers = driver.find_elements(by='xpath', value='//div[@class="story__copy-container"]')

# driver.find_element(by='xpath', value='//div[@class="story__copy-container"]/a/p')
for container in containers:
    title = container.find_element(by='xpath', value='./a/p').text
    subtitle = container.find_element(by='xpath', value='./a/h3').text

    container.find_element(by='xpath', value='./a').get_attribute('href')