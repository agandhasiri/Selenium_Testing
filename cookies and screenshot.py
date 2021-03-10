from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path="C:\Drivers\drivers\chromedriver")                            # open chrome browser
driver.maximize_window()                                                                                # maximize the window
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")                                  # go to a website
time.sleep(3)


c = driver.get_cookies()
print("No of Cookies =",len(c) )
print(c)


driver.get_screenshot_as_file("C:\Desktop\sem 4\screenshot.png")
driver.quit()
