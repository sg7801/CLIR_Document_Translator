import string
import Utility
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import nltk.data
from numpy import dot
import French_To_English
import English_To_French
import IBM_Model1_EM
from numpy.linalg import norm
nltk.download('stopwords')

def cosine(string1) :
    average = 0
    if (string1 == 1): #French
        tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')
        with open("Dataset/output.txt") as k:
            output = k.readlines()
        with open("Dataset/actual.txt") as p:
            actual = p.readlines()
        
        output_tokenized = English_To_French.sen_tokenizer(output)
        actual_tokenized = English_To_French.sen_tokenizer(actual)
                
        output_sentence = list()
        actual_sentence = list()
        
        for line in output_tokenized :
            a = tokenizer.tokenize(line)
            for sentence in a :
                output_sentence.append(sentence)
        
        for line in actual_tokenized :
            a = tokenizer.tokenize(line)
            for sentence in a :
                actual_sentence.append(sentence)
        
        no_of_sentence = len(output_sentence)
        stopwords_list = stopwords.words('french')
        
        for index in range(no_of_sentence) :
                    
            list1 =[];
            list2 =[] 
            
            A = word_tokenize(output_sentence[index].lower())
            B = word_tokenize(actual_sentence[index].lower())
            
            A_set = {words for words in A if not words in stopwords_list}  
            B_set = {words for words in B if not words in stopwords_list}
    
            rvector = A_set.union(B_set)
            
            for word in rvector: 
                if word in A_set: list1.append(1) # create a vector 
                else: list1.append(0) 
                if word in B_set: list2.append(1) 
                else: list2.append(0) 
                    
            c = 0
            # cosine formula  
            for i in range(len(rvector)): 
                    c+= list1[i]*list2[i] 
               
            if (norm(list1)*norm(list2)) > 0:
                cosine_sim = c/(norm(list1)*norm(list2))
            average += cosine_sim/no_of_sentence
            
            print("\ncosine=",cosine_sim)

        print("\nfinal cosine similarity: ",average) 


    elif(string1 ==2) :
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        with open("Dataset/output.txt") as k:
            output = k.readlines()
        with open("Dataset/actual.txt") as p:
            actual = p.readlines()
        
        output_tokenized = French_To_English.sen_tokenizer(output)
        actual_tokenized = French_To_English.sen_tokenizer(actual)
        
        output_sentence = list()
        actual_sentence = list()
        
        for line in output_tokenized :
            a = tokenizer.tokenize(line)
            for sentence in a :
                output_sentence.append(sentence)
        
        for line in actual_tokenized :
            a = tokenizer.tokenize(line)
            for sentence in a :
                actual_sentence.append(sentence)
        
        no_of_sentence = len(actual_sentence)
        stopwords_list = stopwords.words('english')
        
        for index in range(no_of_sentence) :
                    
            list1 =[];
            list2 =[] 
            try:
                A = word_tokenize(output_sentence[index].lower())
                B = word_tokenize(actual_sentence[index].lower())
            except IndexError:
                continue
            
            A_set = {words for words in A if not words in stopwords_list}  
            B_set = {words for words in B if not words in stopwords_list}
    
            rvector = A_set.union(B_set)
            
            for word in rvector: 
                if word in A_set: list1.append(1) # create a vector 
                else: list1.append(0) 
                if word in B_set: list2.append(1) 
                else: list2.append(0)          
            c = 0
            
            # cosine formula  
            for i in range(len(rvector)): 
                    c+= list1[i]*list2[i] 
                    
            if (norm(list1)*norm(list2)) > 0:
                cosine_sim = c/(norm(list1)*norm(list2))
            average += cosine_sim/no_of_sentence
            print("\ncosine=",cosine_sim)

        print("\nfinal cosine similarity: ",average) 
