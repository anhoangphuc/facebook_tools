import time
import os
import json

from selenium import webdriver
from selenium.webdriver import ChromeOptions


class FacebookAccount():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        opt = ChromeOptions()
        opt.add_argument('--no-sandbox')
        opt.add_argument('--headless')

        self.driver = webdriver.Chrome(chrome_options=opt)
        self.driver.get('https://www.facebook.com/login.php')

    def login(self):
        element_email = self.driver.find_element_by_id('email')
        element_password = self.driver.find_element_by_id('pass')

        element_email.send_keys(self.email)
        element_password.send_keys(self.password)

        login_button = self.driver.find_element_by_id('loginbutton')
        login_button.click()

        #wait for login success
        time.sleep(5)

    def get_cookies(self):
        return self.driver.get_cookies()

    def get_cookie(self, a_cookie):
        return self.driver.get_cookie(a_cookie)

    def get_c_user(self):
        return self.get_cookie('c_user')['value']

    def execute_script(self, file_path, script):
        if script != '':
            return self.driver.execute_script(script)

        if file_path != '':
            with open(str(os.path.join('.', 'resources', file_path)), 'r') as script_file:
                return self.driver.execute_script(script_file.read())

        return self.driver.execute_script('')


    def get_token(self):
        redirected_url = f'https://m.facebook.com/{self.get_c_user()}'
        self.driver.get(redirected_url)
        time.sleep(5)
        self.execute_script(file_path='', script="token = ''")
        self.execute_script(file_path='get_token_script.txt', script='')
        token = ''
        cnt = 0
        while token == '' and cnt < 10:
            time.sleep(5)
            token = self.execute_script(file_path='', script='return token')

        return token

    def close(self):
        self.driver.close()
