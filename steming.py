# import these modules
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

'''
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))

# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better", pos ="a"))
'''
#print(lemmatizer.lemmatize("countries"))
def lematize(word):
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(word)


