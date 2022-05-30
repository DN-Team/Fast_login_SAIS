'''
DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

'''
import selenium
from selenium import webdriver
import configparser
import sys

config = configparser.ConfigParser()
config.read("..\\config.ini")

url = 'http:\\\\portal.knu.edu.tw\\knue2\\'

Type = config['login_web']['type']
sid = config['login_web']['username']
upwd = config['login_web']['password']


def login():
    driver = webdriver.Ie()
    driver.implicitly_wait(3)
    driver.get(url)

    login_type = driver.find_element_by_xpath(
        "//input[@name='USER_STATUS' and @value='%s']" % (Type))  # value='2' student / value='1' teacher
    login_type.click()

    username = driver.find_element_by_name('EMPNO')
    username.send_keys(sid)

    pwd = driver.find_element_by_name('loginPassword')
    pwd.send_keys(upwd)

    login = driver.find_element_by_id('button1')
    login.click()


if __name__ == '__main__':
    login()
    sys.exit(0)
