from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)


#TC 1.1
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
#TC 1.2
driver.get("https://www.saucedemo.com/cart.html")
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Ilham")
driver.find_element(By.ID, "last-name").send_keys("Makarim")
driver.find_element(By.ID, "postal-code").send_keys("59462")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()
driver.find_element(By.ID, "back-to-products").click()

#TC2
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
driver.get("https://www.saucedemo.com/cart.html")
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "continue").click()

#TC3
driver.get("https://www.saucedemo.com/cart.html")
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Ilham")
driver.find_element(By.ID, "continue").click()

#TC4
driver.get("https://www.saucedemo.com/cart.html")
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Ilham")
driver.find_element(By.ID, "last-name").send_keys("Makarim")
driver.find_element(By.ID, "continue").click()

driver.close()