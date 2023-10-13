import os           #This is a module need to handle the directory function to read the file from a directory
import re           #This is a module known as Regular Expession to filter the text requiured
import steming      #this is a module written externally in the filepath and imported as user_defiend module
import porter       #This is a module written externally in the filepath and imported as user_defined module

'''
'readStopWords' is a function created to read the List of StopWords from the given directory and return the list of stop words. 
'''
def readStopWords():
    try:
        fp=open("Stopwords.txt",'r',encoding='utf-8')
        readWords=fp.read()
        if readWords:
            ListOfStopWords= readWords.split("\n")
        else:
            print("No Such Files found Stopwords.txt")
    except Exception as e:
        print("Unexpected Error Occured ",e)
    finally:
        fp.close()
    return ListOfStopWords


'''
getTheListOfDir is a parameterized function works by using the data from a given parameter 'path' which represents the path of the directory and returns
the list of files in the given directory. 
'''                    
def getTheListOfDir(path):
    try:
        dir_list = os.listdir(path)
    except Exception as e:
        print("Unexpected Error Occured ",e)
    return dir_list

'''
processTheNestedData is a parameterized function works by using the data from a given parameter 'dataInTextFiles',which is nested list
is processed and made as simple list
'''
def processTheNestedData(dataInTextFiles):
    try:
        processedListOfWords=[]
        for i in range(len(dataInTextFiles)):
            for j in range(len(dataInTextFiles[i])):
                    processedListOfWords.append(dataInTextFiles[i][j])
        processedListOfWords=list(processedListOfWords)
        processedListOfWords.sort()
    except Exception as e:
        print("Unexpected Error has Occured ",e)
    return processedListOfWords

'''
getTheDataFromTextFiles is a two parameters function works by using the data from given parameters, which contain path and directory name
In this function we read the data and use the regu;larexpression to extract the words in the data and update the letter casing and send the 
data to process the nested list of words
'''
def getTheDataFromTextFiles(path,dir_list):
    dataInTextFiles=[]
    try:
        filepath=path+dir_list
        fp=open(filepath,'r',encoding='utf-8')
        readData=fp.read()
        if readData:
                dataInTextFiles.append(re.findall(r"\b[a-z]{4,}+\b",readData.lower()))
                
        else:
            print("No data found in the text file ",dir_list)
    except Exception as e:
            print("Exception occured ",dir_list,e)
    finally:
        fp.close()
    return processTheNestedData(dataInTextFiles)  


'''
lemmatizeTheWords is a function works to filter the list morphologically using the libraries
In this two libraries are used Stemming and Porter
Porter is imported modeule written externally in the directory
'''

def lemmatizeTheWords(ListOfWords):
    try:
        portedList=[]
        for i in range(len(ListOfWords)):
            portedList.append(porter.porterCaller(steming.lematize(ListOfWords[i])))
        portedList=list(portedList)
        portedList.sort()
    except Exception as e:
        print("Unexpected Error has occured ",e)
    return portedList


'''
removeTheStopWords is function which removes the stopwords present in the list given as parameter to this function
'''
def removeTheStopWords(portedList,stopWords):
    try:
        UniqueVocab=[]
        for i in range(len(portedList)):
            if portedList[i] not in stopWords:
                UniqueVocab.append(portedList[i])
            else:
                continue
    except Exception as e:
        print("Unexpected error occured ",e)
    return UniqueVocab
    

'''
WriteintoFile is a function which  writes the data into the files with the file name corresponding to the input files where the data
is collected. 
'''
def WriteintoFile(UniqueVocab,dir1):
    try:
        Words=[]
        out_dir="OutputFiles\\Output_"+dir1
        file1 = open(out_dir, "w")
        #with open(out_dir,'+w') as f:
        for i in range(len(UniqueVocab)):
            Words.append(UniqueVocab[i])
        
        for i in range(len(Words)):
            file1.write(Words[i])
            file1.write("\n")
            #pickle.dump(Words,f)
        
    except Exception as e:
        print("Unexpected Error has Occured ",e)
    finally:
        file1.close()
        
#def calculateTheTermFrequency(UniqueVocab):
            

'''
Driver or main fucntion which handels all the process
This function executes first automatically
'''         
if __name__=="__main__":
    try:
        path = "D://Information Retrieval//Assignment 4//InputDocuments//"
        dir1=getTheListOfDir(path)
        for i in range(len(dir1)):
            UniqueVocab=[]
            UniqueVocab=removeTheStopWords(lemmatizeTheWords(getTheDataFromTextFiles(path,getTheListOfDir(path)[i])),readStopWords())
            WriteintoFile(UniqueVocab,dir1[i])
    except Exception as e:
        print("Unexpected Error has occured ",e)
    finally:
       input("Please Press any key to Exit")
        

