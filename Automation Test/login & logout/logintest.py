from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class login(unittest.TestCase):

    def set_login(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_login_positive(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://itera-qa.azurewebsites.net")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID, "Username").send_keys("dfebri")
        self.driver.find_element(By.ID, "Password").send_keys("Azura#01")  
        self.driver.find_element(By.NAME, value= "login").click()        
        time.sleep(3)

    def test_login_negative(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://itera-qa.azurewebsites.net")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, value= "Login").click()
        self.driver.find_element(By.ID, "Username").send_keys("dcahya")
        self.driver.find_element(By.ID, "Password").send_keys("Azura90")  
        self.driver.find_element(By.NAME, value= "login").click()        
        time.sleep(3)
    
    def test_logout(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://itera-qa.azurewebsites.net")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, value= "Login").click()
        self.driver.find_element(By.ID, "Username").send_keys("dfebri")
        self.driver.find_element(By.ID, "Password").send_keys("Azura#01")  
        self.driver.find_element(By.NAME, value= "login").click() 
        time.sleep (1)
        self.driver.find_element(By.LINK_TEXT, value= "Log out").click()
        time.sleep (3)

if __name__ == "__main__":
    unittest.main()
