import selenium
import pyperclip
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from config import CHROME_PROFILE_PATH
# options = webdriver.ChromeOptions()
# options.add_argument(CHROME_PROFILE_PATH)

# chrome_options=webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path=r'C:/Users/kashi/AppData/Local/Temp/Temp1_chromedriver_win32.zip/chromedriver.exe')

driver.get("https://web.whatsapp.com")
driver.maximize_window()
with open('grp names.txt', 'r', encoding='utf8') as file:
    groups = [group.strip() for group in file.readlines()]
with open('msg.txt', 'r', encoding='utf8') as file:
    msg = file.read()
# print(msg)
# print(groups)

for group in groups:
    search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    # search_box = driver.find_element("class name","_3FRCZ")
    search_box = WebDriverWait(driver, 500).until(
        EC.presence_of_element_located((By.XPATH, search_box_xpath))
    )
    # search_box.send_keys(group)
    text_to_be_searched = 'accommodation'
    search_box.send_keys('text_to_be_searched')
    # search_box.send_keys(Keys.RETURN)

    time.sleep(60)
    search_box.clear()
    
    messages = driver.find_elements(By., ".message-text")
    for message in messages:
        if 'accommodation' in message.text:
            text_with_acc = pyperclip.copy(message.text)
            print(text_with_acc)

    #pyperclip.copy(group)
    #search_box.send_keys(Keys.CONTROL + "v")

    time.sleep(1.5)
    #group_title_xpath = f'//span[@title="{group}"]'
    #group_title = driver.find_element("xpath", group_title_xpath)
    #group_title.click()

    time.sleep(1.5)
    #message_box_xpath = '//div[@title="Type a message"]'
    #message_box = driver.find_element("xpath", message_box_xpath)
    #pyperclip.copy(msg)

    #message_box.send_keys(Keys.CONTROL + "v")
    #message_box.send_keys(Keys.ENTER)
    time.sleep(2)
