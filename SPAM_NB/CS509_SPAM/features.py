import os
import numpy as np
from collections import Counter

def make_Dictionary(training_dir):
    findEmails = [os.path.join(training_dir,f) for f in os.listdir(training_dir)] 
    allWords = []       
    for mail in findEmails:    
        with open(mail) as m:
            for i,line in enumerate(m):
                if i > 1:
                    words = line.split()
                    allWords += words
    dictionary = Counter(allWords)
    removeList = dictionary.keys()
    for item in list(removeList):
        if item.isalpha() == False: 
           del dictionary[item]
        elif len(item) == 1:
           del dictionary[item]

    dictionary = dictionary.most_common(1500)
    return dictionary

def extract_features(training_dir,dictionary): 
    
    trainingFiles = [os.path.join(training_dir,f) for f in os.listdir(training_dir)]
    features_matrix = np.zeros((len(trainingFiles),1500))
    docID = 0;
    for file in trainingFiles:
      with open(file) as fileopen:
        for i,line in enumerate(fileopen):
          if i > 1:
            words = line.split()
            for word in words:
              compte = 0
              for i,d in enumerate(dictionary):
                if d[0] == word:
                  compte = i
                  features_matrix[docID,compte] = words.count(word)
        docID = docID + 1     
    return features_matrix
