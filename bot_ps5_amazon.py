from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from decouple import config

driver = webdriver.Chrome('..\..\Downloads\chromedriver_win32\chromedriver')

# Check PS5 URL and change it if needed
driver.get("https://www.amazon.fr/PlayStation-%C3%89dition-Standard-DualSense-Couleur/dp/B08H93ZRK9/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps5&qid=1613820665&sr=8-1&th=1")

# Click on accept cookies button
driver.find_element_by_id("sp-cc-accept").click()

# Mouse hover on account list
ActionChains(driver).move_to_element(driver.find_element_by_id("nav-link-accountList")).perform()

# Click on Sign In button
driver.find_element_by_xpath("//*[@id='nav-flyout-ya-signin']/a").click()

# Put email adress in email input
element = driver.find_element_by_id("ap_email")
element.send_keys(config("EMAIL_AMAZON"))

# Click on the continue button
driver.find_element_by_id("continue").click()

# Put password in password input
element = driver.find_element_by_id("ap_password")
element.send_keys(config("PWD_AMAZON"))

# Click on the sign in submit button
driver.find_element_by_id("signInSubmit").click()

# Wait 30 seconds if there is verification to do
time.sleep(30)

# Infinite loop
while True:
    time.sleep(2)

    # Check if there is the add to cart button
    if not driver.find_elements(By.ID, "add-to-cart-button"):

        # Refresh if it isn't
        driver.refresh()
    else:

        # Click on the add to cart button
        driver.find_element_by_id("add-to-cart-button").click()

        # Click on the go to basket button
        btn = WebDriverWait(driver, 30
            ).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[4]/div[6]/div[1]/div[9]/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/span/span/input")))

        btn.click()
        # CAREFUL BY UNCOMMENTING this line it will buy the PS5 as soon as it's available
        # driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/span/span/input").click()
        break
time.sleep(1000)
