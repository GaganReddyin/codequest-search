import requests

siteUrl = "https://www.codechef.com/problems/" 

questionNameList = []
questionLinkList = []
questionDifficultyList = []

def writeToFile():
    file = open('questionLinks/questionsLinkCodechef.txt','w')
    for x in range(questionLinkList.__len__()):
        file.write(questionLinkList[x]+"\n")
    file.close()
    
def getJSON(apiUrl):
    url = apiUrl
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Request failed with status code:", response.status_code)
    
def getData():
    try:
        totalPages = 211
        print("Total Pages : ", totalPages)
        
        #Fetching data from each page
        for page in range(0, totalPages):
            print(
                f"    ----------->  Fetching data from page : {page} of {totalPages-1} \n\n"
            )
            apiUrl = f"https://www.codechef.com/api/list/problems?page={page}&limit=20&sort_by=difficulty_rating&sort_order=asc&search=&category=rated&start_rating=0&end_rating=5000&topic=&tags=&group=all&"
            jsonData = getJSON(apiUrl)
            for x in jsonData['data']:
                pageUrl = siteUrl + x['code']
                questionLinkList.append(pageUrl)
        
        print("    ----------->  done all pages")
        print(f" total {questionLinkList.__len__()} question fetched")  
        writeToFile()
            
    except Exception as e:
        print("    ----------->  Error in getData() : ", e)
        return    
    

if __name__ == "__main__":
    getData()
