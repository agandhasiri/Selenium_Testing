from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path="C:\Drivers\drivers\chromedriver")                            # open chrome browser
driver.maximize_window()                                                                                # maximize the window
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")                                  # go to a website
time.sleep(3)

driver.find_element_by_id("tool-2").click()

element = driver.find_element_by_id("continents")
drop = Select(element)
print(len(drop.options))
all_options = drop.options
for option in all_options:
    print(option.text)
drop.select_by_visible_text("North America")

time.sleep(3)
driver.quit()
