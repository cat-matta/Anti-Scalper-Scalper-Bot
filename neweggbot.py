from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import csv
'''
What does this bot do? Simple, it goes onto NewEgg and buys something for you. You can sign in(which is better because then your shipping and payment stuff is saved).
Or you can just add the thing to the cart and get to the checkout, putting in the credit card info is still in progress because its a different way of input.
Steps:
-goes onto newegg
-refresh the page to get rid of annoying popup
-searches for {whatever}. OR  you can have it go to the product link right away, which is better.
-selects the first instance of the product
-adds the item to cart
-checks out
-chooses guest checkout. Again, you signed in, its better
-adds shipping info and selects the suggested shipping 
-

'''

chrome_options = Options()

'''
Defining Selenium WebDriver with Chrome
'''
# chromedriver_path = *FILE DIRECTORY PATH TO chrome.exe*
webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get("https://newegg.com") #goes to new eggg


#sign in stuff
#put in a different link, since newegg generates a different sign in everytime
newegg_sign_in="https://secure.newegg.com/identity/signin?tk=c37130e1614e4945a0a4ec1f96b22cce31184"
webdriver.get(newegg_sign_in)

#new egg has anti-bot measures, so a page refresh is needed
#new egg also generates random sign in links!!! So you have to put this link everytime
webdriver.get(newegg_sign_in)


secretemail=open("email.txt",'r') #put your email in a file called email.txt
myemail=secretemail.read() #put email in a separate file
email=webdriver.find_element_by_name("signEmail")
email.send_keys(myemail)

sleep(1)

SIGN_IN_XPATH="/html/body/div[5]/div/div[2]/div/div/div[1]/form/div/div[3]/button"
signin=webdriver.find_element_by_xpath(SIGN_IN_XPATH)
signin.click()

print("Email is in!")
sleep(0.5) #our bot moves too quick, so wait a bit

secretpass=open("pass.txt",'r')
mypass=secretpass.read()
password=webdriver.find_element_by_name("password")
password.send_keys(mypass)

LOGIN_BUTTON_XPATH="/html/body/div[5]/div/div[2]/div/div/div[2]/form/div/div[3]/button"
button_login=webdriver.find_element_by_xpath(LOGIN_BUTTON_XPATH)
button_login.click()


print("We're in boiiis!!!")

sleep(2)

#webdriver.get("https://newegg.com")
product_link="https://www.newegg.com/blue-green-045496882648-nintendo-switch-bundle/p/N82E16878190873"
webdriver.get(product_link) # its better to put the link of the product right away, this here searches
print("refresh...")
sleep(5)
webdriver.get(product_link)

'''
#this is to search for stuff
item_to_search_for="Nintendo Switch"
search_ari_label='[aria-label="Keywords, Model # or Item #"]'
#search=webdriver.find_element_by_name("d")
search=webdriver.find_elements_by_css_selector(search_ari_label)
search[0].click()
search[0].send_keys(item_to_search_for)

print("searching for {}...".format(item_to_search_for))

SEARCH_BUTTON_XPATH="/html/body/header/div[1]/div[3]/div[1]/form/div/div[3]/button"
#SEARCH_BUTTON_XPATH="/html/body/div[8]/header/div[1]/div[3]/div[1]/form/div/div[3]/button"
sleep(0.25)
search_it=webdriver.find_element_by_xpath(SEARCH_BUTTON_XPATH)
search_it.click()

print("button clicked...")

webdriver.execute_script("window.scrollTo(0, 200);")
print("scrolling down...")
sleep(5)
print("scrolled down...")



PRODUCT_XPATH="/html/body/div[8]/div[3]/section/div/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/button"
first_product=webdriver.find_element_by_xpath(PRODUCT_XPATH)
first_product.click()
print("clicked first product...")
'''

sleep(3)
#/html/body/div[10]/div[3]/div[1]/div/div/div[1]/div[1]/div[4]/div/div[2]/button

# I think the add to cart XPATH is different for every product???
ADD_TO_CART_BUTTON_XPATH="/html/body/div[10]/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/div/div[2]/button"
add_to_cart=webdriver.find_element_by_xpath(ADD_TO_CART_BUTTON_XPATH)
add_to_cart.click()
print("added to cart...")


sleep(0.75)

NO_THANKS_BUTTON_XPATH="/html/body/div[10]/div[3]/div[2]/div/div/div/div[3]/button[1]"

no_thanks=webdriver.find_element_by_xpath(NO_THANKS_BUTTON_XPATH)
no_thanks.click()
print("no thanks...")

sleep(1.25)


VIEW_CART_XPATH="/html/body/div[10]/div[3]/div[2]/div/div/div[2]/div[2]/button[2]"
view_cart=webdriver.find_element_by_xpath(VIEW_CART_XPATH)
view_cart.click()

print("viewing cart...")

sleep(0.75)

html = webdriver.find_element_by_tag_name('html')
html.send_keys(Keys.END) #goes all the way down the page
print("going to end...")
sleep(2)
print("went to end...")
sleep(0.5)
CHECKOUT_XPATH="/html/body/div[8]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button"
checkout_button=webdriver.find_element_by_xpath(CHECKOUT_XPATH)
checkout_button.click()
print("checking out...")
sleep(1)
'''
GUEST_CHECKOUT_XPATH="/html/body/div[5]/div/div[2]/div/div/div[1]/form[2]/div[2]/div/button"
guest_checkout=webdriver.find_element_by_xpath(GUEST_CHECKOUT_XPATH)
guest_checkout.click()
print("guest checkout..")

print("scrolling down...")
html=webdriver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
print("scrolled down...")

sleep(2)

ADD_NEW_ADDRESS_CHECKOUT="/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/i"
add_new_address=webdriver.find_element_by_xpath(ADD_NEW_ADDRESS_CHECKOUT)
add_new_address.click()
print("adding new address...")
sleep(0.5)

print("putting first name...")
first_name=webdriver.find_element_by_name("FirstName")
first_name.send_keys("JEFF")

print("putting last name...")
last_name=webdriver.find_element_by_name("LastName")
last_name.send_keys("GEOF")

print("putting address1...")
address=webdriver.find_element_by_name("Address1")
address.send_keys("420 69th Street")

print("putting address2...")
address2=webdriver.find_element_by_name("Address2")
address2.send_keys("69")

print("putting city...")
city=webdriver.find_element_by_name("City")
city.send_keys("Brooklyn")

print("putting zip code...")
zipc=webdriver.find_element_by_name("ZipCode")
zipc.send_keys("11220")


print("putting phone#...")
phone=webdriver.find_element_by_name("Phone")
phone.send_keys("347-420-6969")

print("putting email...")
email=webdriver.find_element_by_name("Email")
email.send_keys("haha.im.a.bot@gmail.com")

print("putting in a state...")
STATE_XPATH="/html/body/div[6]/div/div/div/div/div[2]/form/div[2]/div[9]/label[2]/select"
state=webdriver.find_element_by_xpath(STATE_XPATH)
state.click()
state.send_keys("New York")

print("scrolling down...")
html=webdriver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
print("scrolled down...")

SAVE_BUTTON_XPATH="/html/body/div[6]/div/div/div/div/div[3]/button[2]"
save_button=webdriver.find_element_by_xpath(SAVE_BUTTON_XPATH)
save_button.click()
print("saved info...")
sleep(1)


USE_ADDRESS_XPATH="/html/body/div[6]/div/div/div/div/div[3]/button[2]"
use_address=webdriver.find_element_by_xpath(USE_ADDRESS_XPATH)
use_address.click()
print("used suggested address...")

sleep(1)
CONT_TO_DELIV_XPATH="/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[3]/button"
cont_deliv=webdriver.find_element_by_xpath(CONT_TO_DELIV_XPATH)
cont_deliv.click()
print("continued to delivery options...")

sleep(1)

CONT_TO_PAYMENT_XPATH="/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div/div[2]/div/div[3]/button"
cont_payment=webdriver.find_element_by_xpath(CONT_TO_PAYMENT_XPATH)
cont_payment.click()
print("continued to payment...")
sleep(0.5)

html=webdriver.find_element_by_tag_name("html")
html.send_keys(Keys.END)
print("scolled down...")

sleep(0.5)

ADD_NEW_CREDIT_CARD_XPATH="/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div/div"
add_new_credit=webdriver.find_element_by_xpath(ADD_NEW_CREDIT_CARD_XPATH)
add_new_credit.click()
print("adding new credit...")
sleep(1)

#NEEDS FIXING
# CARD_HOLDER_CLASSNAME="Cardholder Name"
#CARD_HOLDER_CLASSNAME_XPATH="form-text is-wide"
# card_holder=webdriver.find_elements_by_css_selector("[aria-label='Cardholder Name']")#.send_keys("JEFF GEOF")
#card_holder[0]="JEFF GEOF"
# print(card_holder)

#card_holder_ari_label='[aria-label="Cardholder Name"]'
#card_holder="input.form-text.is-wide[label='Cardholder Name']"
card_holder="//input[@type='text'][@aria-label='Cardholder Name']"

card_holder=webdriver.find_elements_by_css_selector(card_holder)
#card_holder.append("WOW")
card_holder.click()
card_holder.send_keys("JEFF GEOF")
print(card_holder)
# print("putting in expiration month...")
# MONTH_XPATH="/html/body/div[6]/div/div[2]/div[1]/div[4]/label[2]/select"
# month=webdriver.find_element_by_xpath(MONTH_XPATH)
# month.click()
# month.send_keys("06")

CCV_XPATH="/html/body/div[6]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/div/label/div[4]/input"

# print("putting in expiration year...")
# YEAR_XPATH="/html/body/div[6]/div/div[2]/div[1]/div[5]/label/select"
# year=webdriver.find_element_by_xpath(YEAR_XPATH)
# year.click()
# year.send_keys("2030")
'''
html=webdriver.find_element_by_tag_name("html") #scrolls down all the way to the end
html.send_keys(Keys.END)
print("scolled down...")

print("Now all you gotta do is put the CVV number and click place order...")

print("done!!!")



