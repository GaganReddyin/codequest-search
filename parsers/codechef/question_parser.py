import time
from bs4 import BeautifulSoup
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By as by

body_id = "#problem-statement"
heading_class = "._titleStatus__container_1dtux_838"

def writeToFile2(heading,body,index,pageUrl):
    file = open(f'questionContent/questionCodechef{index}.txt','w',encoding='utf-8')
    file.write(heading + "\n" + body)
    file.close()
    
    file = open(f'questionLinks/questionsLink_{index}.txt','w',encoding="utf-8")
    file.write(pageUrl)
    file.close()
    
    file = open(f'questionHeadings/questionsName_{index}.txt','w',encoding="utf-8")
    file.write(heading)
    file.close()
    
def openBrowser(url):
    print("    ----------->  Opening Browser")
    Options = webdriver.ChromeOptions()
    Options.add_argument("--ignore-certificate-errors")
    Options.add_experimental_option("excludeSwitches", ["enable-logging"])
    Options.add_argument("--incognito")
    Options.add_argument("--headless")
    
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=Options)
    
    driver.get(url)
    driver.maximize_window()
    return driver

def closeBrowser(browser):
    print("    ----------->  Closing Browser")
    browser.quit()
    
def singlePageData(pageUrl,index):
    try :
        browser = openBrowser(pageUrl)
        time.sleep(2)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((by.CSS_SELECTOR, body_id)))
        time.sleep(1)
        bodyContent = browser.find_element(by.CSS_SELECTOR, body_id)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        heading = soup.find_all("h1")[0]
        if(bodyContent.text):
            writeToFile2(heading.text,bodyContent.text,index,pageUrl)
            print("    ----------->  saving data ")
        time.sleep(1)
        return True
        
    except Exception as e:
        print(f"    ----------->  Error in singlePageData({e}) ")
        return False
    
def getArrLinks():
    file = open('../questionLinks/questionsLinkCodechef.txt','r')
    arr = []
    for line in file:
        arr.append(line)
    file.close()
    return arr
    
def main_function():
    index = 1
    arr = getArrLinks()
    # getting data from single page
    for link in arr:
        success = singlePageData(link,index)
        if(success):
            index = index + 1
    
if __name__ == "__main__":
    main_function()
