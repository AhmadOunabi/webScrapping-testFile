from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def Scrapper():
    driver=webdriver.Chrome()
    driver.get("https://flat.io/auth/signin")
    time.sleep(2)
    
    '-------login to the flat.io--------'
    
    driver.find_element(By.ID,'emailInput').send_keys('ahmad_ounabi@yahoo.com')
    driver.find_element(By.NAME,'password').send_keys('AdminAdmin123')
    driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[3]/div/div[3]/form/button').click()
    
    time.sleep(5000)

Scrapper()


