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
driver.get("https://www.auchan.fr/sony-console-ps5-edition-standard/p-c1315865?awc=7728_1611766383_8ad32be0af4b4b32b905f4534aacf8fd&utm_medium=affiliation&utm_source=zanox&utm_campaign=generique&utm_content=0&utm_term=285077")
time.sleep(80)
while True:
    time.sleep(2)
    if driver.find_elements_by_class_name("error-container--title"):
        driver.refresh()
    else:
        winsound.Beep(2500, 1000)
        # NOT DOING ANYTHING ONLY REFRESHING CONTINUE THE CODE IF YOU WANT (PROJECT IS OPEN-SOURCE SO SHARE WITH OTHER BY CREATING A PULL REQUEST)
        break
winsound.Beep(2500, 1000)
time.sleep(1000)
