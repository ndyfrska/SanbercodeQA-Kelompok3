from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://itera-qa.azurewebsites.net")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.LINK_TEXT, value= "Login").click()
time.sleep(3)
driver.find_element(By.ID, "Username").send_keys("dcahya")
driver.find_element(By.ID, "Password").send_keys("Azura90")

time.sleep(3)
driver.find_element(By.NAME, value= "login").click()
time.sleep(5)

driver.quit()
