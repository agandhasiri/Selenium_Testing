from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="C:\Drivers\drivers\chromedriver")                            # open chrome browser
driver.maximize_window()                                                                                # maximize the window
driver.get("https://store.dexcom.com/")                                                                 # go to a website
print(driver.title)                                                                                     # for the title of website
#time.sleep(3)                                                                                           # add time to view the actions
driver.implicitly_wait(10)                                                                              # implicit wait till the elements are displayed
driver.find_element_by_xpath("//*[@id='openid-connect-login-form']/div/div/div[2]/div[2]/a").click()    # click on create account
# time.sleep(3)
driver.quit()                                                                                           # close the website