import json
import sys
import time
import random

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()
driver.get("https://web.whatsapp.com")
print("\n\nLog into whatsapp in the newly opened browser by scanning the code")
name = input("Enter the name of the contact and press enter: ")
emoji_no = 20
try:
    new_no = input(
        "Enter the no of emojis and press enter (Press enter without entering value to use default value of 20): ")
    if not new_no == '':
        emoji_no = int(new_no)
except ValueError:
    print("No of emojis should be an integer")
    sys.exit()

with open('simple-emoji-list.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

count = 0
emojis = []

for keys, values in data.items():
    if count >= emoji_no:
        break
    for emoji in values:
        emoji_code = chr(int(emoji['code'].replace('U+', '0x').lower(), 16))
        emojis.append(emoji_code)
        count += 1
        if count >= emoji_no:
            break

random.shuffle(emojis)

find_button = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/button')
ActionChains(driver).click(find_button).send_keys(name).send_keys(Keys.ENTER).perform()

count =0
delay = 3
try:
    message_element = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))
    text_element = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    while True:
        if count>=emoji_no:
            break
        for emoji in emojis:
            driver.execute_script('''
                    element = document.evaluate('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    element.innerText = arguments[0]
                    ''', emoji)
            text_element.send_keys('a')
            text_element.send_keys(Keys.BACKSPACE)
            text_element.send_keys(Keys.ENTER)
            count+=1
            if count>=emoji_no:
                break


except TimeoutException:
    print("Page loading timeout: The page did not load for more than 3 seconds")
