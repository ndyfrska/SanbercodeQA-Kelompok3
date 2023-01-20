from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class dashboard(unittest.TestCase):

    def set_dashboard(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_dashboard_practice(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://itera-qa.azurewebsites.net")
        self.driver.maximize_window()
        # time.sleep (3)
        self.driver.find_element(By.LINK_TEXT, "Home").click()
        self.driver.find_element(By.CSS_SELECTOR, "body > div > div.jumbotron > p:nth-child(4) > a").click()          
        time.sleep(2)

    def test_dashboard_practice(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://itera-qa.azurewebsites.net")
        self.driver.maximize_window()
        # time.sleep (3)
        self.driver.find_element(By.LINK_TEXT, "Practice").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p/button").click()    
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/p/button").click() 
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/p/button").click()    
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/p/button").click()      
        time.sleep(2)

    def test_dashboard_testautomation(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://itera-qa.azurewebsites.net")
        self.driver.maximize_window()
        # time.sleep (3)
        self.driver.find_element(By.LINK_TEXT, "Test Automation").click()     
        time.sleep(2)
    
    def test_dashboard_tutorial(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://itera-qa.azurewebsites.net")
        self.driver.maximize_window()
        # time.sleep (3)
        self.driver.find_element(By.LINK_TEXT, "Tutorial").click()    
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
