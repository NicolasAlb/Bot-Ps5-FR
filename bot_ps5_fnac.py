from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import winsound
from decouple import config

# TO IMPROVE, GET KICKED BECAUSE REFRESH BY FNAC AFTER SOME TIME

driver = webdriver.Chrome('..\..\Downloads\chromedriver_win32\chromedriver')
driver.get("https://www.fnac.com/Console-Sony-PS5-Edition-Standard/a14119956/w-4")
time.sleep(30)
driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[2]/div/div[2]/div[2]/a").click()
element = driver.find_element_by_id("email")
element.send_keys(config('EMAIL_FNAC'))
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/div[2]/button").click()
time.sleep(2)
element = driver.find_element_by_id("password")
element.send_keys(config('PWD_FNAC'))
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/div[4]/button").click()
while True:
    time.sleep(2)
    if not driver.find_elements_by_xpath("/html/body/div[2]/div/div[1]/div[2]/section/ul[2]/li/div/div[2]/div[1]/div[2]/button"):
        driver.refresh()
    else:
        driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/section/ul[2]/li/div/div[2]/div[1]/div[2]/button").click()
        btn = WebDriverWait(driver, 30
            ).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div[1]/a")))
        btn.click()
        btn = WebDriverWait(driver, 30
            ).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div/div/div[2]/section/div[3]/form/button")))
        btn.click()
        winsound.Beep(2500, 1000)
        break

time.sleep(1000)