from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

siteUrl = "https://leetcode.com/problems/"
pageTitle = "Problems - LeetCode"

questionNameList = []
questionLinkList = []
questionDifficultyList = []

def writeToFile():
    file = open('../questionContent/leetcodeContent.txt','w')
    for x in range(questionLinkList.__len__()):
        file.write(questionLinkList[x]+"\n")
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
    
def fetchPageData(pageUrl):
    browser = openBrowser(pageUrl)
    time.sleep(3)
    pageSource = browser.page_source
    wait = WebDriverWait(browser, 10)
    wait.until(EC.title_contains(pageTitle))
    soup = BeautifulSoup(pageSource, "html.parser")
    
    if (browser.title == pageTitle):
        print("    ----------->  parsing data ")
        
        newSoup = BeautifulSoup(pageSource, "html.parser")
        QuestionBlock = newSoup.find('div', role="rowgroup")
        QuestionList = QuestionBlock.find_all('div', role="row")
        
        for question in QuestionList:
            row = question.find_all('div', role="cell")
            questionName = row[1].find('a').text
            questionUrl = row[1].find('a')['href']
            questionUrl = "https://leetcode.com" + questionUrl
            questionDifficulty = row[4].find('span').text   
            questionLinkList.append(questionUrl)
            questionDifficultyList.append(questionDifficulty)
            questionNameList.append(questionName)   
            
        print("    ----------->  saving data ")
        time.sleep(1)
        print("    ----------->  done ")
        closeBrowser(browser)
    else :
        print("    ----------->  connection failed ")
        return
    
def getData():
    try:
        browser = openBrowser(siteUrl)
        time.sleep(2)
        pageSource = browser.page_source
        wait = WebDriverWait(browser, 10)
        wait.until(EC.title_contains(pageTitle))
        soup = BeautifulSoup(pageSource, "html.parser")
        
        if (browser.title == pageTitle):
            
            #fetching total number of pages
            totalQuestions = soup.find('nav', role="navigation" ,class_="mb-6 md:mb-0 flex flex-nowrap items-center space-x-2")
            # print(totalQuestions)
            index = totalQuestions.__len__() - 2
            totalPages = int(totalQuestions.contents[index].text)
            print("Total Pages : ", totalPages)
            closeBrowser(browser)
            
            #Fetching data from each page
            for page in range(1, totalPages+1):
                print(
                    f"    ----------->  Fetching data from page : {page} of {totalPages} \n\n"
                )
                pageUrl = siteUrl + '?page=' + str(page)
                fetchPageData(pageUrl)  
            
            print("    ----------->  done all pages")
            print(f" total {questionNameList.__len__()} question fetched")  
            writeToFile()
        
        else :
            print("    ----------->  connection failed ")
            return
            
    except Exception as e:
        print("    ----------->  Error in getData() : ", e)
        return    
    

if __name__ == "__main__":
    getData()
