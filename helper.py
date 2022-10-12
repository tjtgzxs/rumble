import json
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import Constant
import redis
import random


def save_cookie(driver, path):
    with open(path, 'w') as filehandler:
        json.dump(driver.get_cookies(), filehandler)


def load_cookie(driver, path):
    with open(path, 'r') as cookiesfile:
        cookies = json.load(cookiesfile)
    for cookie in cookies:
        driver.add_cookie(cookie)


def judge_cookie(path):
    if not os.path.exists(path):
        return False
    with open(path, 'r') as cookiesfile:
        cookies = json.load(cookiesfile)
    if len(cookies) == 0:
        return False
    else:
        if cookies[0]['expiry'] == 0 or cookies[0]['expiry'] < int(time.time()):
            return False
        return True


def login_by_stackoverflow(driver, username, password):
    driver.get('https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
    sleep(3)
    print('login')
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
    driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
    wait = WebDriverWait(driver, 50)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierNext"]')))
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    sleep(3)
    num = 1
    while True:
        try:
            print(str(num) + "\n")
            driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
            break
        except:
            input_again(driver, username, wait)
            num += 1
    # driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="passwordNext"]')))
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    sleep(2)
    if driver.current_url == 'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f':
        print(False)
        return False
    else:
        print(True)
        return True


def input_again(driver, username, wait=None):
    time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="next"]')))
    driver.find_element_by_xpath('//*[@id="next"]/div').click()
    time.sleep(5)
    driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
    time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierNext"]')))
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    time.sleep(5)
    return True


def login_again(browser, wait):
    browser.find_element(By.XPATH, '//input[@type="email"]').send_keys("tjtgjohnson@gmail.com")
    time.sleep(Constant.USER_WAITING_TIME)
    browser.find_element(By.XPATH, '//*[@id="identifierNext"]').click()
    time.sleep(Constant.USER_WAITING_TIME)
    browser.find_element(By.XPATH,'//input[@type="password"]').send_keys("1990Jtwmy")
    time.sleep(Constant.USER_WAITING_TIME)
    browser.find_element(By.XPATH, '//*[@id="passwordNext"]').click()
    time.sleep(Constant.USER_WAITING_TIME)
    save_cookie(browser, Constant.COOKIE_FILE)
    print("2 end")

def get_keyword(keyword):
    arr = str.split(',')
    return random.choice(arr)

