import time
import names
from decouple import config
from selenium import webdriver


HOME = config('HOME')
# page = webdriver.Firefox()
page = webdriver.Chrome(executable_path=HOME + '/chromedriver/chromedriver')
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/signup/')

# Login
search = page.find_element_by_id('id_username')
username = names.get_first_name().lower()
search.send_keys(username)

search = page.find_element_by_id('id_email')
email = username + '@spark.com'
search.send_keys(email)

search = page.find_element_by_id('id_password')
search.send_keys('demodemo')

search = page.find_element_by_id('id_confirm_password')
search.send_keys('demodemo')

search = page.find_element_by_class_name('btn-primary')
search.click()

time.sleep(2)
page.quit()
