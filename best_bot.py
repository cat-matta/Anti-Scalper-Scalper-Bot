from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randint
import csv
'''
Setting up Chrome options for use - necessary for chrome to be used in Repl.it
'''
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless') # allows for running in a silent window
'''
Defining Selenium WebDriver with Chrome
'''
# chromedriver_path = *FILE DIRECTORY PATH TO chrome.exe*
webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get("https://www.bestbuy.com/identity/signin?token=tid%3A76cd7b18-1f73-11eb-a502-121fb7f40979")
#sleep(3)

secretemail=open("email.txt",'r')
myemail=secretemail.read()
email=webdriver.find_element_by_name("fld-e")
email.send_keys(myemail)
secretpass=open("pass.txt",'r')
mypass=secretpass.read()
password=webdriver.find_element_by_name("fld-p1")
password.send_keys(mypass)

LOGIN_BUTTON_XPATH="/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[4]/button"
button_login=webdriver.find_element_by_xpath(LOGIN_BUTTON_XPATH)
button_login.click()

sleep(5)
X_BUTTON_XPATH="/html/body/main/div[2]/div[5]/div/div/div[1]/div/div/div/div/button"

x_it_out=webdriver.find_element_by_xpath(X_BUTTON_XPATH)
x_it_out.click()
#CLICK_AWAY_XPATH="/html/body/main/div[2]/div[4]/div[1]/div[1]/div/div"
#body=webdriver.find_element_by_xpath(CLICK_AWAY_XPATH)
#body.click()
sleep(3)

search=webdriver.find_element_by_name("st")
search.send_keys("Nintendo Switch")

SEARCH_BUTTON_XPATH="/html/body/div[2]/div/div/div/header/div[2]/div[1]/div/div[2]/div/div[1]/div/div/form/button[2]"
search_it=webdriver.find_element_by_xpath(SEARCH_BUTTON_XPATH)
search_it.click()

FIRST_PRODUCT_XPATH="/html/body/div[4]/main/div[10]/div/div/div/div/div/div/div[2]/div[2]/div[5]/div/div/div/div[6]/ol/li[1]/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div[3]/div/h4/a"
first_product=webdriver.find_element_by_xpath(FIRST_PRODUCT_XPATH)
first_product.click()