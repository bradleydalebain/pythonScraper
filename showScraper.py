#s
My Drive
#!/home/Documents/python/scraper-master/scrape3/python3.6
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import youtube_dl
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess

proxies = {
'http' : 'http://192.168.43.1:8000',
'https' : 'https://192.168.43.1:8000',
}




options = webdriver.ChromeOptions()
options.binary_location='/usr/bin/google-chrome'
#options.add_argument('headless')
options.add_argument('--proxy-server=192.168.43.1:8000')
browser = webdriver.Chrome(chrome_options=options)

class logi:

    URL = 'http://www.nick.com/'


    def login(browser):
        URL = 'http://www.nick.com/'
    #request initial page
        browser.get(URL)
    #locate and click nav bar
        browser.find_element_by_class_name('is-clickable').click()
    #Click to get sign in page
        browser.find_element_by_class_name('footer-item-text-link').click()
    #click "getting started" button
        browser.find_element_by_class_name('button').click()
    #wait
        time.sleep(2)
    #locate and click cox login link
        cox = browser.find_element_by_xpath('//*[@id="extraMvpdWrapper"]/ul/li[4]/a').click()
        #get window count, and use it to switch to new tab
        windows_before  = browser.current_window_handle
        WebDriverWait(browser, 5).until(EC.number_of_windows_to_be(2))
        windows_after = browser.window_handles
        new_window = [x for x in windows_after if x != windows_before][0]
        browser.switch_to_window(new_window)
    #wait
        time.sleep(4)
        uname = 'jsrulz'
        psswd = 'Iszack91314'
    #username and password location and entry
        user = browser.find_element_by_xpath('//*[@id="container"]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/form/input[1]')
        password = browser.find_element_by_xpath('//*[@id="container"]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/form/input[2]')
        time.sleep(1)
        user.send_keys(uname)
        time.sleep(1)
        password.send_keys(psswd)
        time.sleep(1)
    #click submit
        browser.find_element_by_xpath('//*[@id="container"]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/form/input[6]').submit()
        input('')
        nick(browser)

        def nick(browser):
            browser.switch_to_window(windows_before)
            browser.get('http://www.nick.com/spongebob-squarepants/episodes/')
            source = requests.get('http://www.nick.com/spongebob-squarepants/episodes/')
            soup = BeautifulSoup(source.content, 'html.parser')
            routes = soup.find_all('a', attrs={'class':'route'}, href=True)
            for route in route:
                if 'full-episode' in route.get('href'):
                    print(route)


    login(browser)
