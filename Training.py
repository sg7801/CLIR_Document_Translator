import IBM_Model1_EM
import string 
import Utility
import numpy as np
from nltk.tokenize import word_tokenize

def tokenize_sentences(sentences, index):
    final = list()
    word_dict = {}
    reversed_dict = {}
    language_order = 0
    count = 0 
    
    translation_matrix = dict((ord(char), None) for char in string.punctuation)
    
    for a in sentences[:index]:
        if count == 0:
            a = a.replace(u'\ufeff', '')
            count+=1
        
        # removing the punctuation
        a = a.translate(translation_matrix)
        tokens = word_tokenize(a.lower())
        
        sentence_output = ""
        
        for token in tokens:
            if token not in word_dict:
                word_dict[token] = language_order
                reversed_dict[language_order] = token
                language_order+=1
            sentence_output = sentence_output + token + " "
        sentence_output = sentence_output[:(len(sentence_output) - 1)]
        
        final.append(sentence_output)
    final[0] = final[0].replace(u'\ufeff', '')
    
    return final, word_dict, reversed_dict

def model_trainer():
    with open("Training_Data/English.txt", encoding="utf8") as f:
        english_data = f.readlines()
    with open("Training_Data/French.txt", encoding="utf8") as l:
        french_data = l.readlines()
        
    curr_english_data = list()
    curr_french_data = list()
    
    for sentence_curr in range(len(english_data)):
        if sentence_curr > 79992:
            break
        current_english_sentence = english_data[sentence_curr].split()
        current_training_sentence = french_data[sentence_curr].split()
        
        if len(current_english_sentence) < 25 and len(current_training_sentence) < 25:
            curr_english_data.append(english_data[sentence_curr])
            curr_french_data.append(french_data[sentence_curr])
            
            
    english_data = curr_english_data.copy()
    french_data = curr_french_data.copy()
    maximum_translations = 3000
    
    french_sentences, french_word_dict, reversed_french_word_dict = tokenize_sentences(french_data, maximum_translations)
    english_sentences, english_word_dict, reversed_english_word_dict = tokenize_sentences(english_data, maximum_translations)
    
    translate_english_french = IBM_Model1_EM.expectation_maximization(french_word_dict, english_word_dict, french_sentences, english_sentences)
    
    total_french_occurence = translate_english_french.shape[0]
    total_english_occurence = translate_english_french.shape[1]
    
    english_map = {}
    french_map = {}
    
    
    for english_curr in range(total_english_occurence):
        maxi = -100
        j = 0
        for french_curr in range(total_french_occurence):
            if translate_english_french[french_curr][english_curr] > maxi:
                maxi = translate_english_french[french_curr][english_curr]
                j = french_curr
        english_map[reversed_english_word_dict[english_curr]] = reversed_french_word_dict[j]

    for french_curr in range(total_french_occurence):
            maxi = -100
            j = 0
            
            for english_curr in range(total_english_occurence):
                if translate_english_french[french_curr][english_curr] > maxi:
                    maxi = translate_english_french[french_curr][english_curr]
                    j = english_curr
            
            french_map[reversed_french_word_dict[french_curr]] = reversed_english_word_dict[j]

    np.save("Trained_Data/French_To_English",french_map)
    np.save("Trained_Data/English_To_French",english_map)      
