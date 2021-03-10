from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path="C:\Drivers\drivers\chromedriver")                            # open chrome browser
driver.maximize_window()                                                                                # maximize the window
driver.get("https://store.dexcom.com/")                                                                 # go to a website
print(driver.title)                                                                                     # for the title of website
time.sleep(3)                                                                                           # add time to view the actions
driver.implicitly_wait(10)                                                                              # implicit wait till the elements are displayed
driver.find_element_by_xpath("//*[@id='openid-connect-login-form']/div/div/div[2]/div[2]/a").click()    # click on create account

driver.find_element_by_id("edit-name").send_keys("akhil")
driver.find_element_by_id("edit-mail").send_keys("akg.gmail.com")
driver.find_element_by_id("edit-pass-pass1").send_keys("akg")
driver.find_element_by_id("edit-pass-pass2").send_keys("akg")
driver.find_element_by_class_name("option").click()
driver.find_element_by_xpath("//*[@id='recaptcha-anchor' ]/div[1]").click()
time.sleep(3)
driver.quit()