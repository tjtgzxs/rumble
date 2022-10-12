from typing import DefaultDict, Optional
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import time
import os
import platform
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Constant
import helper
from send import main as send_msg
from send import send_img
import configparser
import random
class upload:
    def __init__(self):
        try:
            config = configparser.ConfigParser()
            config.read(Constant.BASE_DIR + "conf.ini")
            options = ChromeOptions()
            mimvp_proxy = {

                'ip': '127.0.0.1',  # ip

                'port_http': 1080,  # http, https

                'port_socks': 1080,  # socks5
            }
            proxy_https_argument = '--proxy-server=http://{ip}:{port}'.format(ip=mimvp_proxy['ip'], port=mimvp_proxy[
                'port_http'])  # http, https (无密码，或白名单ip授权，成功)
            options.add_argument(proxy_https_argument)
            proxy_socks_argument = '--proxy-server=socks5://{ip}:{port}'.format(ip=mimvp_proxy['ip'], port=mimvp_proxy[
                'port_socks'])  # socks5 (无密码，或白名单ip授权，失败)
            options.add_argument(proxy_socks_argument)
            self.browser = uc.Chrome(browser_executable_path=Constant.BROWSER_EXECUTABLE_PATH,
                                 driver_executable_path=Constant.DRIVE_EXECUTABLE_PATH,
                                 options=options,headless=config.getboolean("WEBDRIVER","headless"))
            logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.INFO)
        except Exception as e:
            self.browser.save_screenshot(Constant.BASE_DIR + "/screenshot.png")
            send_img(Constant.BASE_DIR + "/screenshot.png",)
            send_msg("获取浏览器错误："+str(e))
            return -1
    def process(self,username,password,video_path):
        try:
            self.login(username,password)
            url=self.upload(video_path)
            return url
        except Exception as e:
            self.browser.save_screenshot(Constant.BASE_DIR + "/screenshot.png")
            send_img(Constant.BASE_DIR + "/screenshot.png",)
            send_msg("上传视频的错误："+str(e))
            return -1


    def login(self, username, password):
        self.browser.get(Constant.BASE_URL)
        time.sleep(Constant.USER_WAITING_TIME)
        if helper.judge_cookie(Constant.COOKIE_FILE):
            self.logger.info("1111")
            helper.load_cookie(self.browser, Constant.COOKIE_FILE)
            time.sleep(Constant.USER_WAITING_TIME)
            self.browser.refresh()
            time.sleep(Constant.USER_WAITING_TIME)
        else:
            self.logger.info("22222")
            self.browser.find_element(By.XPATH, Constant.LOGIN_BUTTON).click()
            time.sleep(Constant.USER_WAITING_TIME)
            self.browser.find_element(By.XPATH, Constant.USERNAME_INPUT).send_keys(username)
            self.browser.find_element(By.XPATH, Constant.PASSWORD_INPUT).send_keys(password)
            self.browser.find_element(By.XPATH, Constant.LOGIN_CONFIRM).click()
            time.sleep(Constant.USER_WAITING_TIME)
            helper.save_cookie(self.browser, Constant.COOKIE_FILE)

    def upload(self, video_file):
        self.logger.info("开始上传:"+str(video_file))
        time.sleep(Constant.USER_WAITING_TIME)
        # self.browser.find_element(By.XPATH, Constant.UPLOAD_BUTTON).click()
        self.browser.get(Constant.UPLOAD_URL)
        absolute_video_path = str(video_file)

        self.browser.find_element(By.XPATH, Constant.VIDEO_INPUT).send_keys(
            absolute_video_path)
        time.sleep(Constant.USER_WAITING_TIME+random.randint(0,9))
        self.browser.find_element(By.XPATH, Constant.TITLE_INPUT).send_keys("funny & cute animals")
        time.sleep(Constant.USER_WAITING_TIME + random.randint(0, 9))
        video_description = "funny & cute animals,very happy"
        video_description = video_description.replace("\n", Keys.ENTER)
        time.sleep(Constant.USER_WAITING_TIME + random.randint(0, 9))
        self.browser.find_element(By.ID, "description").send_keys(video_description)
        time.sleep(Constant.USER_WAITING_TIME + random.randint(0, 9))
        self.browser.find_element(By.ID, "tags").send_keys("cute,dogs")
        time.sleep(Constant.USER_WAITING_TIME + random.randint(0, 9))

        while True:
            # end = self.browser.find_element(By.XPATH, Constant.PERCENT).find("100")
            end = self.browser.find_element(By.CLASS_NAME, "green_percent").get_attribute("style")
            self.logger.info(end)
            if not end == "width: 100%;":
                time.sleep(Constant.USER_WAITING_TIME)
            else:
                break
        self.browser.find_element(By.ID, Constant.FORM_BUTTON_1).click()
        time.sleep(Constant.USER_WAITING_TIME+random.randint(0,9))
        self.browser.find_element(By.XPATH, Constant.SELECT_1).click()
        time.sleep(Constant.USER_WAITING_TIME + random.randint(0, 9))
        self.browser.find_element(By.XPATH, Constant.CRIGHTS).click()
        time.sleep(Constant.USER_WAITING_TIME + random.randint(0, 9))
        self.browser.find_element(By.XPATH, Constant.CTERMS).click()
        time.sleep(Constant.USER_WAITING_TIME + random.randint(0, 9))
        self.browser.find_element(By.ID, "submitForm2").click()
        time.sleep(Constant.USER_WAITING_TIME+random.randint(0,9))
        return self.browser.find_element(By.XPATH, Constant.RESEULT_URL).get_attribute("href")

    def close(self):
        self.browser.close()
