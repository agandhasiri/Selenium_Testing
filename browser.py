from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\drivers\chromedriver")                           # open chrome browser
driver.maximize_window()                                                                               # maximize the window
driver.get("https://store.dexcom.com/")                                                                # go to a website
driver.quit()                                                                                          # close the window
