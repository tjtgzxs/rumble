# browser_executable_path=""
import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__)) + os.path.sep
BASE_CHROME_PATH=r"C:\Users\Johnson\Desktop\chrome-win\chrome-win"
BROWSER_EXECUTABLE_PATH=BASE_CHROME_PATH+"\chrome.exe"
DRIVE_EXECUTABLE_PATH=BASE_CHROME_PATH+"\chromedriver.exe"
BASE_URL="https://rumble.com/"
USER_WAITING_TIME=3
COOKIE_FILE = BASE_DIR+"cookies.json"
LOGIN_BUTTON="/html/body/header/div/button[@class='header-user']"
USERNAME_INPUT="//*[@id='login-username']"
PASSWORD_INPUT="//*[@id='login-password']"
LOGIN_CONFIRM="//*[@id='loginForm']/button[@type='submit']"
UPLOAD_BUTTON="/html/body/header/div/button[@class='header-upload']"
UPLOAD_URL="https://rumble.com/upload.php"
VIDEO_INPUT="//*[@id='Filedata']"
TITLE_INPUT="//*[@id='title']"
PERCENT="//*[@class='num_percent']"
FORM_BUTTON_1="submitForm"
SELECT_1="/html/body/main/div/div/div/section/form[2]/div/div[2]/div[1]/div"
RESEULT_URL="//*[@id='view']/a"
CRIGHTS="//label[@for='crights']"
CTERMS="//label[@for='cterms']"

