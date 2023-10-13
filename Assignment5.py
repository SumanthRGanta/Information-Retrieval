from collections import defaultdict
import Assignment4


#to get the file names fromthe output directory
def getTheInputFileNames():
    path="OutputFiles"
    #MainDoc.getTheListOfDir(path)
    listOfFiles=Assignment4.getTheListOfDir(path)
    return listOfFiles,path


#it creates the unique list of the avialable vocabulary in the output documents
def Create_A_UniqueListOfTerms(listOfFiles):
    uniqueWords=[]
    for i in range(len(listOfFiles)):
        fp=open(path+"\\"+listOfFiles[i], 'r')
        uniqueWords=uniqueWords+(fp.read()).split("\n")
    uniqueWords=list(set(uniqueWords))
    uniqueWords.remove("")
    uniqueWords.sort()
    return uniqueWords
    #print(uniqueWords)
        
#It calculates the frequency of all the terms
def freqOfTerm(doc_id,term,path):
    #read the term from the document
    with open(path+"\\"+doc_id, 'r') as f:
        doc=list(f.read().lower().split("\n"))
        doc.remove("")
        return doc.count(term)

#Create the dictionary order for the terms with their term and document frequency   
def Create_A_Dictionary_Of_Terms(listOfFiles,path,uniqueList):
    dictOfTerms=defaultdict(dict)
    for i in range(len(uniqueList)):
        for j in range(len(listOfFiles)):
            doc_id=listOfFiles[j]
            freq =freqOfTerm(doc_id,uniqueList[i],path)
            if freq>0:
                dictOfTerms[uniqueList[i]].update({doc_id:freq})
    return dictOfTerms


#Driver method
if __name__=="__main__":
    listOfFiles,path=getTheInputFileNames()
    uniqueVocab=Create_A_UniqueListOfTerms(listOfFiles)
    dictOfOutput=Create_A_Dictionary_Of_Terms(listOfFiles,path,uniqueVocab)
    listOfVocab=dict(dictOfOutput)
    with open("output.txt", 'w') as f:  
        for key, value in listOfVocab.items():  
            f.write('%s:%s\n' % (key, value))
    
