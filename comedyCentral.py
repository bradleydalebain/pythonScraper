<<<<<<< HEAD
=======
''' #!/home/Documents/python/scraper-master/scrape3/python3.6 '''
>>>>>>> b20681a1344221907d1fea1518eb3dbfacac2f2d
import time
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
URL = 'http://www.cc.com/episodes/scdnse/stand-up-specials-carlos-mencia--no-strings-attached-season-1-ep-101'
options = webdriver.ChromeOptions()
options.binary_location='/usr/bin/google-chrome'
# options.add_argument('headless')
options.add_argument('user-data-dir=selenium')
options.add_argument('--proxy-server=192.168.43.1:8000')
browser = webdriver.Chrome(chrome_options=options)
browser.get(URL)
<<<<<<< HEAD

def show_page(browser):
    shows = []
    num_episodes = []
    browser.get('http://www.cc.com/full-episodes')
    show_titles = browser.find_elements_by_class_name('title')
    for title in show_titles:
        shows.append(title.text)
    while '' in shows:
        shows.remove('')
    episode_num = browser.find_elements_by_class_name('count')
    for episodes in episode_num:
        num_episodes.append(episodes.text)
    while '' in num_episodes:
        num_episodes.remove('')
    display = list(zip(shows,num_episodes))
    pprint(display)
def login(browser):
    uname = 'jsrulz'
    psswd = 'Iszack91314'
=======
urls = []

def show_page(browser):
    browser.get('http://www.cc.com/')
def login(browser):
    uname = ''
    psswd = ''
>>>>>>> b20681a1344221907d1fea1518eb3dbfacac2f2d
    unamefield = browser.find_element_by_xpath('//*[@id="container"]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/form/input[1]')
    passfield = browser.find_element_by_xpath('//*[@id="container"]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/form/input[2]')
    sub = browser.find_element_by_xpath('//*[@id="container"]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/form/input[7]')
    unamefield.send_keys(uname)
    passfield.send_keys(psswd)
    sub.click()
    browser.switch_to_window(browser.window_handles[0])
    page = browser.current_url
    cont = input('Press enter to download video')
    if 'y' or 'Y' in cont:
        GetContent(browser)
    elif 'n' or 'N' in cont:
        show_page(browser)
#def getlogin(browser):
    time.sleep(1)
    coxpage = browser.find_element_by_xpath('//*[@id="primaryListWrapper"]/ul/li[4]/a')
    coxpage.click()
    browser.switch_to_window(browser.window_handles[1])
    wait = WebDriverWait(browser, 120)
    wait.until(EC.presence_of_element_located((By.ID, 'pf-search-input')))
    login(browser)


def GetContent(browser):
    urls = []
    ydl_opts = {'config-location' : '~/.config/youtube-dl/youtube-dl.conf' , 'outtmpl': '~/Videos/%(title)s.%(ext)s', 'external_downloader' : 'axel', 'external_downloader_args' : '-n 5'}
    src = browser.find_element_by_name('original-source')
    srctext = src.get_attribute('content')
    urls.append(src)
    print(srctext)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([srctext])

show_page(browser)
#getlogin(browser)
"""
proxies = {
'http' : 'http://192.168.43.1:8000',
'https' : 'https://192.168.43.1:8000',
}
"""
