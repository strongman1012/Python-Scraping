from selenium.webdriver.common.by import By
def get_good_words(bad_letters,words,middle_letter):
    """finds all words in the list 'words' that contain middle_letter
    at least once and does not contain any bad letters"""
    good_words = []
    for each in words:
        each = each.lower()
        is_valid = True
        for bad_char in bad_letters:
            if bad_char in each:
                is_valid = False
                break
        if is_valid and middle_letter in each:
            good_words.append(each)
    return good_words

def get_bad_letters(good_letters):
    """returns all the letters that are not present in the
    spelling bee hive"""
    bad_letters = []
    for letter in 'qwertyuiopasdfghjklzxcvbnm':
        if letter not in good_letters:
            bad_letters.append(letter)
    return bad_letters
def get_good_letters_and_buttons(driver):
    """returns a dict of buttons mapped to each letter as well as
    a list of all 6 of the letters that are in the hive"""
    hive = driver.find_element(By.CLASS_NAME, 'hive')
    good_letters = []
    btns = {}
    for pol in hive.find_elements(By.TAG_NAME, 'svg'):
        btn = pol.find_element(By.CLASS_NAME, 'cell-letter')
        letter = btn.get_attribute('innerHTML')
        btns[letter] = pol
    for cell in hive.find_elements(By.CLASS_NAME, 'cell-letter'):
        good_letters.append(cell.get_attribute('innerHTML'))
    return (good_letters, btns)
def get_words():
    """gets list of english words, exculding proper nouns"""
    with open('english_no_proper', 'r') as f:
        words = []
        for word in f:
            word = word.replace('\n','')
            words.append(word)
    return words
