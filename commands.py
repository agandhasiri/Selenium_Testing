from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path="C:\Drivers\drivers\chromedriver")                            # open chrome browser
driver.maximize_window()                                                                                # maximize the window
driver.get("https://store.dexcom.com/")                                                                 # go to a website
time.sleep(3)                                                                                           # add time to view the actions
driver.implicitly_wait(10)                                                                              # implicit wait till the elements are displayed
driver.find_element_by_xpath("//*[@id='openid-connect-login-form']/div/div/div[2]/div[2]/a").click()    # click on create account


driver.find_element_by_class_name("option").click()

b = driver.find_element_by_xpath("//*[@id='menu-2136-1']/a").is_displayed()
c = driver.find_element_by_xpath("//*[@id='edit-account']/div[1]/label").is_displayed()
d = driver.find_element_by_class_name("option").is_enabled()

print(driver.title)
driver.back()
print(driver.title)
driver.implicitly_wait(10)
e = driver.find_element_by_class_name("logo").is_displayed()
time.sleep(2)
driver.forward()
print(driver.title)
time.sleep(2)




print(b,c,d, e)
driver.quit()
