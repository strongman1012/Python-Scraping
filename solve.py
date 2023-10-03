import selenium
import time
import sys
import argparse
import word_proc
import streamlit as st
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# argparse stuff
parser = argparse.ArgumentParser()
parser.add_argument("--browser", help="Browser used to solve spellingbee, default is firefox", default='firefox')
parser.add_argument("-l","--login", action='store_true', help='use to manually log in to NYT')
parser.add_argument("-v", "--verbose", action="store_true", help='print words that are being tried')
parser.add_argument("-S","--no_solve",action="store_true", help='do not solve, only list words in terminal')
args = parser.parse_args()

def create_driver(browser):
    if browser == 'firefox':
        driver = selenium.webdriver.Firefox()
    elif browser == 'chrome':
        driver = selenium.webdriver.Chrome()
    elif browser == 'edge':
        driver = selenium.webdriver.Edge()
    else:
        print(f'unsupported browser called: {args.browser}')
        print(f'contact me at github or open an issue to get {args.browser} support')
        sys.exit(1)
    return driver

def open_login_page(driver):
    driver.get('https://myaccount.nytimes.com/auth/enter-email?redirect_uri=https%3A%2F%2Fwww.nytimes.com%2Fpuzzles%2Fspelling-bee&amp;response_type=cookie&amp;client_id=games&amp;application=crosswords&amp;asset=navigation-bar')
    return driver 
def solve():
    driver = selenium.webdriver.Chrome()
    url = 'https://www.nytimes.com/puzzles/spelling-bee'
    driver.get(url)
    btns = driver.find_elements(By.TAG_NAME, 'button')
    found = False
    for btn in btns:
        if btn.text.lower() == 'play':
            found = True
            driver.execute_script("arguments[0].click();",btn)
            
    if not found:
        print('unable to get todays spelling-bee, please try again')

    middle_letter = driver.find_element(By.XPATH,"//*[@class='cell-letter' or @class='center']")
    middle_letter = middle_letter.get_attribute('innerHTML')

    good_letters, btns = word_proc.get_good_letters_and_buttons(driver)
    bad_letters = word_proc.get_bad_letters(good_letters)
    # get list of english dictionary words
    words = word_proc.get_words()
    good_words = word_proc.get_good_words(bad_letters, words,middle_letter)
    st.write(good_words)
    driver.close()
 
