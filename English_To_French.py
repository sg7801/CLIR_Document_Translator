import Testing
import Training
import Utility
from nltk.tokenize import word_tokenize
import nltk.data
import string

def sen_tokenizer(list_of_sentences):
    answer = list()
    index = 0
    output_sentence = ""
    
    for sentence in list_of_sentences:
        if index == 0 :
            sentence = sentence.replace(u'\ufeff', '')
            index += 1
        tokens = word_tokenize(sentence.lower())
        
        for token in tokens :
            output_sentence += token + " "
                
        output_sentence = output_sentence[:(len(output_sentence)-1)] 
        answer.append(output_sentence)    

    answer[0] = answer[0].replace(u'\ufeff', '')  
    return answer

def english_to_french():
    tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')
    output = ""
    with open("Dataset/actual.txt") as p:
        data_in_english = p.readlines()
    
    english = sen_tokenizer(data_in_english)
    english_sentence = list()
    
    for eng_sentence in english:
        a = tokenizer.tokenize(eng_sentence)
        for b in a:
            english_sentence.append(b)
    output_file = open("Dataset/output.txt", "w+")
  
    for index in range(len(english_sentence)):
        current_sentence = english_sentence[index]
        current_translated_sentence = Testing.tester(current_sentence,2)
        output_file.write(current_translated_sentence)
        output_file.write(". ")
         
    print("Translation Successful. Translated document is 'output.txt' ")
