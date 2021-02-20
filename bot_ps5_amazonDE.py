from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import winsound
from decouple import config

driver = webdriver.Chrome('..\..\Downloads\chromedriver_win32\chromedriver')
driver.get("https://www.amazon.de/Sony-Interactive-Entertainment-PlayStation-5/dp/B08H93ZRK9/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps5&qid=1611137057&sr=8-1")
driver.find_element_by_id("sp-cc-accept").click()
ActionChains(driver).move_to_element(driver.find_element_by_id("nav-link-accountList")).perform()
driver.find_element_by_xpath("//*[@id='nav-flyout-ya-signin']/a").click()
element = driver.find_element_by_id("ap_email")
element.send_keys(config("EMAIL_AMAZON"))
driver.find_element_by_id("continue").click()
element = driver.find_element_by_id("ap_password")
element.send_keys(config("PWD_AMAZON"))
driver.find_element_by_id("signInSubmit").click()
time.sleep(30)
while True:
    time.sleep(2)
    if not driver.find_elements(By.ID, "add-to-cart-button"):
        driver.refresh()
    else:
        driver.find_element_by_id("add-to-cart-button").click()
        btn = WebDriverWait(driver, 30
            ).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[4]/div[6]/div[1]/div[9]/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/span/span/input")))

        btn.click()
        winsound.Beep(2500, 1000)
        # CAREFUL BY UNCOMMENTING this line it will buy the PS5 as soon as it's available
        # driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/span/span/input").click()
        break
time.sleep(1000)
