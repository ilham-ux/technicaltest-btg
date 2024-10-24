from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

#TC1
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
#TC2
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("ilham_sauce")
driver.find_element(By.ID, "password").send_keys("sauce_indofood")
driver.find_element(By.ID, "login-button").click()
#TC3
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("sauce_indofood")
driver.find_element(By.ID, "login-button").click()
#TC4
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("ilham_sauce")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.close()
