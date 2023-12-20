# Working with Google Chrome Browser
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class browser:
   def __init__(self, url, username, password):
       self.url = url
       self.username = username
       self.password = password
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

   def booting_function(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           return True
       except:
           return False
           print("ERROR : Unable to run the code !")

       
   def fetch_title(self):
       if self.booting_function() == True:
           return self.driver.title
       else:
           return False

   def fetch_url(self):
       if self.booting_function() == True:
           return self.driver.current_url
       else:
           return False


   def login(self):
        try:
            username_locator = "user-name"
            password_locator = "password"
            submit_button = "login-button"

            self.driver.find_element(by=By.ID, value=username_locator).send_keys(self.username)
            print("Username filled")
            sleep(3)
            self.driver.find_element(by=By.ID, value=password_locator).send_keys(self.password)
            print("Password filled")
            sleep(3)
            self.driver.find_element(by=By.ID, value=submit_button).click()
            print("Submit Button clicked")
        except:
            print("ERROR : Something went wrong with Locators !")


     # fetch the entire source code of the webpage
   def fetch_webpage(self):
       if self.booting_function() == True:
           return self.driver.page_source
       else:
           return False



url = "https://www.saucedemo.com/"
username = "standard_user"
password = "standard_user"

test = browser(url, username, password)

print("Title of {a} : ".format(a="the link"),test.fetch_title())
print()
print("URL of {a} : ".format(a="the link"),test.fetch_url())
print()
test.login()
print()
print("View WebPage Details")
print()
print(test.fetch_webpage())




