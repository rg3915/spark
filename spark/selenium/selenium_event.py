import time
from random import choice, randint
from decouple import config
from selenium import webdriver
from gen_address import address
from gen_random_values import gen_string, gen_date, convert_date


HOME = config('HOME')
# page = webdriver.Firefox()
page = webdriver.Chrome(executable_path=HOME + '/chromedriver/chromedriver')
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/login/')

# Login
search = page.find_element_by_id('username')
search.send_keys('admin')

search = page.find_element_by_id('password')
search.send_keys('demodemo')

search = page.find_element_by_class_name('btn-default')
search.click()

page.get('http://localhost:8000/events/')

button = page.find_element_by_class_name('btn-compose')
button.click()

title = choice(['ThinkUP', 'Grupy-SP', 'GDG-SP', 'CSS-SP', 'FrontSP',
                'spark', 'Python Sudeste', 'Python Brasil'])

fields = [
    ['id_title', title],
    ['id_date_start', convert_date(gen_date(2017, 2017))],
    ['id_start', '%s:00' % randint(1, 23)],
    ['id_description', gen_string(30)],
    ['id_address', address()],
]

for field in fields:
    search = page.find_element_by_id(field[0])
    search.send_keys(field[1])
    time.sleep(0.2)


button = page.find_element_by_class_name('btn-post')
button.click()

page.quit()
