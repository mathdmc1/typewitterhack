from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import re

def main():
    driver = webdriver.Chrome()

    driver.get("https://play.typeracer.com/")
    time.sleep(5)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'a[title="Keyboard shortcut: Ctrl+Alt+I"]'))).click()
    time.sleep(5)

    spans = driver.find_elements(By.XPATH, "//span[@unselectable='on']")
    texto = ""
    print(len(spans))
    for span in spans:
        print(span.text)
        
        
    print("Texto a escribir: " +texto)


    escribir=driver.find_element(By.XPATH, "//input[@type='text']")
    time.sleep(5)
    human_type(escribir, texto, min_delay=0.05, max_delay=0.18, space_pause=0.12)
    time.sleep(10)
    driver.quit()










def human_type(el, text, min_delay=0.03, max_delay=0.15, space_pause=0.08):
    el.click()
    try:
        el.clear()
    except Exception:
        pass
    for ch in text:
        if ch == "\n":
            el.send_keys(Keys.ENTER)
        else:
            el.send_keys(ch)
        time.sleep(random.uniform(min_delay, max_delay))
        if ch == " ":
            time.sleep(space_pause)




main()