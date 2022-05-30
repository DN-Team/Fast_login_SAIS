import selenium
from selenium import webdriver
import configparser
import sys

config = configparser.ConfigParser()
config.read("..\\config.ini")

url = 'https:\\\\sts.knu.edu.tw\\'

sid = config['login_web']['username']
upwd = config['login_web']['password']


def login():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.get(url)

    username = driver.find_element_by_id('Editbox1')
    username.send_keys(sid)

    pwd = driver.find_element_by_id('Editbox2')
    pwd.send_keys(upwd)

    login = driver.find_element_by_id('buttonLogOn')
    login.click()


if __name__ == '__main__':
    login()
    sys.exit(0)
