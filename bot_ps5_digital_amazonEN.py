from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from decouple import config

driver = webdriver.Chrome('..\..\Downloads\chromedriver_win32\chromedriver')
driver.get("https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H97NYGP/ref=sr_1_3?dchild=1&keywords=ps5&qid=1611661470&sr=8-3&th=1")
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
        btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "hlb-ptc-btn-native")))
        btn.click()
        # CAREFUL BY UNCOMMENTING this line it will buy the PS5 as soon as it's available
        # driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/span/span/input").click()
        break
time.sleep(1000)
# driver.close()