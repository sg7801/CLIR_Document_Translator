import numpy as np
import Utility
import math
from datetime import datetime

def expectation_maximization(french_word_dict, english_word_dict, french_sentences, english_sentences):
    
    total_french_occurences = len(french_word_dict)
    total_english_occurences = len(english_word_dict)
    
    translate_new_matrix = np.full((len(french_word_dict), len(english_word_dict)), 1/len(english_word_dict), dtype = float)
    translate_old_matrix = np.full((len(french_word_dict), len(english_word_dict)), 1, dtype = float)
    
    count_iterations = 0
    
    while not Utility.convergence(translate_new_matrix, translate_old_matrix, count_iterations):
        count_iterations += 1
        translate_old_matrix = translate_new_matrix.copy()
        total_english_french = np.full((len(french_word_dict), len(english_word_dict)), 0, dtype = float)
        total_foreign = np.full(len(english_word_dict), 0, dtype = float)
        
        for curr_tur, french_sen in enumerate(french_sentences):
            french_sen_words = french_sen.split(" ")
            s_total = np.full(len(french_sen_words), 0, dtype = float)
            
            for curr_word in range(len(french_sen_words)):    
                french_word = french_sen_words[curr_word]
                s_total[curr_word] = 0
                english_sen_words = english_sentences[curr_tur].split(" ")
                
                if french_sen != '' and french_word != '':
                    for eng_word in english_sen_words:    
                        if eng_word == '':
                            continue
                        try:
                            curr_french_in_dict = french_word_dict[french_word]
                            curr_eng_in_dict = english_word_dict[eng_word]
                            s_total += translate_new_matrix[curr_french_in_dict][curr_eng_in_dict]
                        except KeyError:
                            continue
                            
            #collect counts
            french_sen_words = french_sen.split(" ")

            for curr_word in range(len(french_sen_words)):
                french_word =  french_sen_words[curr_word]
                english_sen_words = english_sentences[curr_tur].split(" ")
                
                if french_sen != '' and french_word != '':    
                    for eng_word in english_sen_words:
                        if eng_word == '':
                            continue
                        curr_french_in_dict = french_word_dict[french_word]
                        curr_eng_in_dict = english_word_dict[eng_word]
                    
                        total_english_french[curr_french_in_dict][curr_eng_in_dict] += translate_new_matrix[curr_french_in_dict][curr_eng_in_dict] / s_total[curr_word]
                        total_foreign[curr_eng_in_dict] += translate_new_matrix[curr_french_in_dict][curr_eng_in_dict] / s_total[curr_word]
    
        # estimating the probabilities
        for english_curr in range(total_english_occurences):
            for french_curr in range(total_french_occurences):
                if total_english_french[french_curr][english_curr] != 0 :
                    translate_new_matrix[french_curr][english_curr] = total_english_french[french_curr][english_curr]/ total_foreign[english_curr]
            
    print("Estimation Maximization Algorithm Converged in", count_iterations-1,"iterations")
    return translate_new_matrix

def get_translation_probability(english, foreign, total, english_dict, foreign_dict):
    const = 0.1
    length_english = len(english)
    length_foreign = len(foreign)
    
    result = const/ math.pow((length_foreign + 1), length_english)
    
    for i in range(len(length_english)):
        english_word = english[i]
        
        if english_word in english_dict:
            english_j = english_dict[english_word]
        else:
            print("Word "+ english_word + " not found in the target language dictionary")
            continue
        
        for j  in range(length_foreign):
            foreign_word = foreign[i]
            
            if foreign_word in foreign_dict:
                foreign_i = foreign_dict[foreign_word]
                sum += total[english_j][foreign_i]
            else:
                print("Word " + foreign_word + " not found in the source language dictionary")
        
        answer *= sum
    return answer
