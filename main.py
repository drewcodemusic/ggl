from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser
import time
# create a module to update chromedriver
# create function to wait for element display

def fetchUserData():
    config = configparser.RawConfigParser()
    config.read('config.ini', encoding='utf-8')
    userAccount = config['User']['Account']
    userPwd = config['User']['Pwd']
    userName = config['User']['Name']
    return userAccount, userPwd, userName

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://104.com.tw/')

    acct, pwd, name = fetchUserData()

    driver.find_element(By.XPATH,"//*[contains(@onclick,\"login\")]").click()
    driver.find_element(By.ID,"username").send_keys(acct)
    driver.find_element(By.ID,"password").send_keys(pwd)
    driver.find_element(By.ID,"submitBtn").click()
    time.sleep(30)      # enter otp manually if required

    driver.find_element(By.ID,"myName").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//*[text()=\"My104會員中心\"]").click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])

    assert driver.find_element(By.XPATH,"//*[text()=\""+name+"\"]").is_displayed() == True
    print('[Test passed] User name is displayed in user center correctly')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH,"//*[contains(@onclick,\"logout\")]").click()
    time.sleep(10)  # stop a while to see if logout


