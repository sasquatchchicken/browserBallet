import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver in headless mode
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)  # for some reason firefox still opens a browser window but the changes are there when inspecting 

# Navigate to a website
#your target url goes here
driver.get("insertURL")

# List of cookies to delete
cookies_to_delete = ['browserId', 'countryCode']

# Iterate over cookies and delete if they exist
for cookie_name in cookies_to_delete:
    if cookie_name in [cookies['name'] for cookies in driver.get_cookies()]:
        driver.delete_cookie(cookie_name)

# Perform actions to change browser settings (this might vary based on your specific needs)
# For example, if you want to change a cookie setting:
#driver.add_cookie({'name': 'browserId', 'value': 'my_value'})
driver.add_cookie({'name': 'browserId', 'value': 'e503aa4c-8f10-412f-9823-1fec45e877ac'}) #this UUID was genrated with the use of a random gnerator i made uuid-geo-ip.py 
driver.add_cookie({'name': 'countryCode', 'value': 'JP'}) #i chose japan as my country code 

#driver.refresh()
# Close the browser window
#driver.close()
