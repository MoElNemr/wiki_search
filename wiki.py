from select import select
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

driver_path = 'enter your driver profile path here'
driver = webdriver.Firefox(webdriver.FirefoxProfile(driver_path))

task_name = str(input("what do you want to search for: "))
number_of_phrases = int(input('enter the number of the phrases you want to extract: '))
file_name = str(input('enter the desired file name: '))

driver.get("https://www.wikipedia.org/")

search = WebDriverWait(driver , 5).until(EC.presence_of_element_located((By.ID,"searchInput")))
search.send_keys(task_name)

search_btn = WebDriverWait(driver , 5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/form/fieldset/button")))
search_btn.click()
time.sleep(5)

file = open(f'{file_name}.txt','w')
for i in range(number_of_phrases+2):
    try:
        content = driver.find_element(By.XPATH,f'/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/p[{i}]').text
        for i in content:
            try:
                file.write(str(i))
            except:pass
        file.write('\n\n')
    except:pass

