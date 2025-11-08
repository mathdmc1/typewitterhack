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
    num=0
    for span in spans:
        num+=1
        if num==3:
            texto+=" "+ span.text
            break
        texto+=span.text
        print("Span number: " + str(num))
        print(span.text)
        
        
    print("Texto a escribir: " +texto)


    escribir=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
    time.sleep(9)
    type(escribir, texto)
    time.sleep(10)
    driver.quit()


def type(el, text):
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
        time.sleep(random.randint(1, 3) / 1000)
    




main()