from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime as dt


# create driver
chromedriver_path = '/Users/hoyt/Documents/Python/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_path)

# go to website
url_list = [
    'https://www.amazon.ca/Pop-A-Shot-Home-Single-Shot/dp/B07JWF3W1X/',
    'https://www.amazon.ca/Official-Pop-Shot-Basketball-Construction/dp/B075FC4M29/'
]

for URL in url_list:
    driver.get(URL)

    # find product by id
    product = driver.find_element(by='id', value='productTitle').text

    # find price by class name
    price_dollar = driver.find_element(by='class name', value='a-price-whole').text
    price_cent = driver.find_element(by='class name', value='a-price-fraction').text
    price = float(f"{price_dollar}.{price_cent}")

    # today's date
    today = dt.datetime.today().now().date()

    # save file
    try:
        with open('amazon_product_price.csv', 'a') as output_file:
            output_file.write(f"{today},{product},{price},{URL}\n")
    except FileNotFoundError:
        with open('amazon_product_price.csv', 'w') as output_file:
            output_file.write(f"{today},{product},{price},{URL}\n")

# close browser
driver.quit()
