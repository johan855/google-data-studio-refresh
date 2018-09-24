
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def login(email, password):
    driver.get(URL)
    driver.find_element_by_id("Email").send_keys(email)
    driver.find_element_by_id("next").click()
    time.sleep(7)

    URL1 = driver.current_url

    driver.find_element_by_id("Passwd").send_keys(password)
    driver.find_element_by_id("signIn").click()
    time.sleep(15)

    URL2 = driver.current_url

def refresh():
    try:
        driver.find_element_by_partial_link_text(report_name).click()
    except Exception, e:
        driver.find_element_by_id("submit").click()
        #logger.info('Awaiting confirmation from smartphone...{0}'.format(e))
        time.sleep(15*60)

    time.sleep(7)

    URL3 = driver.current_url

    driver.find_element_by_css_selector("#reporting-app-header > md-toolbar > div > div.rightSide.ng-scope.layout-align-end-center.layout-row > div:nth-child(2) > div").click()



if __name__ == "__main__":

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    URL = "https://accounts.google.com/ServiceLogin?passive=1209600&continue=https://datastudio.google.com/?hl%3Den%23&followup=https://datastudio.google.com/?hl%3Den&hl=en"
    userURL = "https://accounts.google.com/ServiceLogin?passive=1209600&continue=https://datastudio.google.com/?hl%3Den%23&followup=https://datastudio.google.com/?hl%3Den&hl=en#identifier"
    passURL = "https://accounts.google.com/ServiceLogin?passive=1209600&continue=https://datastudio.google.com/?hl%3Den%23&followup=https://datastudio.google.com/?hl%3Den&hl=en#password"
    landingURL = ""
    landingURL2 = ''
    reportURL = ""

    email=''
    password=''
    report_name=''

    login(email, password)
    refresh(report_name)