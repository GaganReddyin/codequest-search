import os
import re              
import string 
import math
import json 
 
def preprocess_name(name):
    #remove number. from the name 
    #removing the digits
    pattern = r'\d+'
    name = re.sub(pattern, ' ', name)
    
    #remove dots and starting and ending spaces
    name = name.replace('.', ' ')
    name = name.strip()
    
    return name

def writeToVacab(vocab):
    with open("document.txt", "w" , encoding="utf-8") as f:
        f.write(vocab)
        f.close()
        
    #store all the words from vocab string to a set
    vocab = vocab.split()
    vocab = set(vocab)
    return vocab
    f.close()
        
def cleaningData(data):
    #lowering the case
    data = data.lower()
    
    # removing the after part of example
    data = data.split("Example 1")[0]
    
    #removing the digits
    pattern = r'\d+'
    data = re.sub(pattern, ' ', data)
    
    #removing punctuations
    translator = str.maketrans('', '', string.punctuation)
    data = data.translate(translator)
    
    #remove extra spaces and next lines
    data = data.replace('\n', ' ')
    data = re.sub(' +', ' ', data)
    
    #remove stop words
    stop_words = ['the', 'a', 'an', 'is', 'are', 'was', 'were', 'has', 'have', 'had', 'been', 'will', 'shall', 'be', 'to', 'of', 'and', 'in', 'that', 'for', 'on', 'with', 'by', 'at', 'from', 'as', 'into', 'through', 'during', 'including', 'until', 'against', 'among', 'throughout', 'despite', 'towards', 'upon']
    data = ' '.join([word for word in data.split() if word not in stop_words])
    
    #remove all the words with length less than 3
    data = ' '.join([w for w in data.split() if len(w)>2])
    
    #remove all the words like its thats you etc
    filler_words = [
    'like', 'um', 'uh', 'ah', 'er', 'well', 'you know', 'actually', 'basically', 'literally',
    'honestly', 'seriously', 'right', 'so', 'anyway', 'anyhow', 'really', 'kind of', 'sort of',
    'pretty', 'quite', 'somewhat', 'just', 'still', 'now','can','this','all','make' ,'there', 'then', 'therefore', 'thus', 'hence','its','you','thats'
    ]

    data = ' '.join([w for w in data.split() if w not in filler_words])
        
    return data

def main():
    document = []
    leetLength = 2000
    codeforcesLength = 6300
    codechefLength = 4000
    
    folder_path = f'../parsers/leetcode/questionContent/'
    for filename in range(1,leetLength):
        try:    
            with open(folder_path + '/questionContentLeetcode' + str(filename) + ".txt", 'r', encoding="utf-8") as f:
                data = f.read()
                data = cleaningData(data)
                document.append(data)
                f.close()
        except:
            print(filename)
            
    folder_path = f'../parsers/codeforces/questionContent/'
    for filename in range(1,codeforcesLength):
        try:    
            with open(folder_path + '/questionCodeforces' + str(filename) + ".txt", 'r', encoding="utf-8") as f:
                data = f.read()
                data = cleaningData(data)
                document.append(data)
                f.close()
        except:
            print(filename)
            
    folder_path = f'../parsers/codechef/questionContent/'
    for filename in range(1,codechefLength):
        try:    
            with open(folder_path + '/questionCodechef' + str(filename) + ".txt", 'r', encoding="utf-8") as f:
                data = f.read()
                data = cleaningData(data)
                document.append(data)
                f.close()
        except:
            print(filename)
                
    var = IDF(document)
    inverse_vocab_map = var[0]
    IDF_map = var[1]
    
    TF_map = TF(document, inverse_vocab_map, IDF_map)
    
    #import questionLink List from parsers -> leetcode -> 
    
    TF_IDF_map = TF_IDF(TF_map, IDF_map)
    
    with open('output.json', 'w') as file:
        json.dump(TF_IDF_map, file)
        
    with open('doc.json', 'w') as file:
        json.dump(document, file)
        
    document_links = []
    document_names = []

    #open the questions Link folder and read all the files and save all the content in a list
    targetDirectory = "../parsers/leetcode/questionLinks/"
    length = len(os.listdir(targetDirectory))

    for i in range(1,leetLength):
        with open(targetDirectory + f'questionsLink_{i}.txt', encoding='utf-8') as f:
            data = f.read()
            document_links.append(data)
            f.close()
            
    targetDirectory = "../parsers/codeforces/questionLinks/"
    length = len(os.listdir(targetDirectory))

    for i in range(1,codeforcesLength):
        with open(targetDirectory + f'questionsLink_{i}.txt', encoding='utf-8') as f:
            data = f.read()
            document_links.append(data)
            f.close()
            
    targetDirectory = "../parsers/codechef/questionLinks/"
    length = len(os.listdir(targetDirectory))

    for i in range(1,codechefLength):
        with open(targetDirectory + f'questionsLink_{i}.txt', encoding='utf-8') as f:
            data = f.read()
            document_links.append(data)
            f.close()
            
    targetDirectory = "../parsers/leetcode/questionHeadings/"
    length = len(os.listdir(targetDirectory))         
            
    for i in range(1,leetLength):
        with open(targetDirectory + f'questionsName_{i}.txt', encoding='utf-8') as f:
            data = f.read()
            data = preprocess_name(data)
            document_names.append(data)
            f.close()
            
    targetDirectory = "../parsers/codeforces/questionHeadings/"
    length = len(os.listdir(targetDirectory))         
            
    for i in range(1,codeforcesLength):
        with open(targetDirectory + f'questionsName_{i}.txt', encoding='utf-8') as f:
            data = f.read()
            data = preprocess_name(data)
            document_names.append(data)
            f.close()
            
    targetDirectory = "../parsers/codechef/questionHeadings/"
    length = len(os.listdir(targetDirectory))         
            
    for i in range(1,codechefLength):
        with open(targetDirectory + f'questionsName_{i}.txt', encoding='utf-8') as f:
            data = f.read()
            data = preprocess_name(data)
            document_names.append(data)
            f.close()
            
    with open('links.json', 'w') as file:
        json.dump(document_links, file)
        
    with open('names.json', 'w') as file:
        json.dump(document_names, file)


def TF_IDF(TF_map, IDF_map):
    TF_IDF_map = {}
    
    for word in IDF_map:
        TF_IDF_map[word] = {}
        for index in TF_map[word]:
            TF_IDF_map[word][index] = TF_map[word][index] * IDF_map[word]
    
    return TF_IDF_map
    
def TF(document, inverse_vocab_map , IDF_map):
    TF_map = {}
    
    for word in IDF_map:
        TF_map[word] = {}
        list = inverse_vocab_map[word]
        
        for index in list:
            para = document[index]
            para = para.split()
            if word in para:
                TF_map[word][index] = para.count(word)/len(para)
            else:
                TF_map[word][index] = 0
    
    return TF_map
    
def IDF(document): 
    IDF_map = {}
    inverse_vocab_map = {}
    index = 0
    
    for para in document:
        para = set(para.split())
        for word in para:
            if word not in inverse_vocab_map:
                inverse_vocab_map[word] = []
            inverse_vocab_map[word].append(index)
            if word in IDF_map:
                IDF_map[word] += 1
            else:
                IDF_map[word] = 1
        index += 1
                
    for word in IDF_map:
        IDF_map[word] = 1 + math.log(len(document)/IDF_map[word])
        
    return inverse_vocab_map, IDF_map

if __name__ == "__main__":
    main()
