import Utility
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import string
import nltk.data
import French_To_English
import English_To_French
nltk.download('stopwords')

def jaccard_coeff(string1):
    average_jaccard = 0
    if (string1 == 1): #French
        tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')
        
        with open("Dataset/output.txt") as f:
            output = f.readlines()
        with open("Dataset/actual.txt") as g:
            actual = g.readlines()
        
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
            z = 0
            length = len(rvector)
            intersection = 0
            union = length

            for i in range(length) :
                intersection += list1[i]*list2[i]

            # jaccard coefficient formula

            jaccard_coefficient = intersection/union 
            average_jaccard += jaccard_coefficient/no_of_sentence
            print("\nJaccard Coefficient : ", jaccard_coefficient) 

        print("\nAverage Jaccard coefficient is ",average_jaccard,"\n")

    elif(string1 == 2): #english
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

        with open("Dataset/output.txt") as f:
            output = f.readlines()
        with open("Dataset/actual.txt") as g:
            actual = g.readlines()
        
        output_lines = French_To_English.sen_tokenizer(output)
        actual_lines = French_To_English.sen_tokenizer(actual)
        
        output_sentence = list()
        actual_sentence = list()
        
        for line in output_lines :
            a = tokenizer.tokenize(line)
            for sentence in a :
                output_sentence.append(sentence)
        
        for line in actual_lines :
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
            
            z = 0
            length = len(rvector)
            intersection = 0
            union = length
            
            for i in range(length) :
                intersection += list1[i]*list2[i]

            # jaccard coefficient formula

            jaccard_coefficient = intersection/union 
            average_jaccard += jaccard_coefficient/no_of_sentence
            print("\nJaccard Coefficient : ", jaccard_coefficient) 

        print("\nAverage Jaccard coefficient is ",average_jaccard,"\n")
