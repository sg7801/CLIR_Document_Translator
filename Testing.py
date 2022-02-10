import numpy as np
from nltk.tokenize import word_tokenize
import string
import Utility
import IBM_Model1_EM

def tokens(sentences):
    translation_matrix = dict((ord(char), None) for char in string.punctuation)
    sentences = sentences.translate(translation_matrix)
    token = word_tokenize(sentences.lower())
    return token

def tester(sentences, choice):
    
    french_to_english_maximised = np.load("Trained_data/French_To_English.npy",allow_pickle = True).item()
    english_to_french_maximised = np.load("Trained_data/English_To_French.npy",allow_pickle = True).item()
    
    if choice == 1:
        french_sentence = tokens(sentences)
        english_sentence = ""
        for word in french_sentence :
            if word in french_to_english_maximised:
                english_sentence = english_sentence + french_to_english_maximised[word] + " "
            else:
                print("word '"+ word +"' does not exist in trained language translation dictionary")
                continue
        return english_sentence
    
    elif choice == 2:
        english_sentence = tokens(sentences)
        french_sentence = ""
        for word in english_sentence :
            if word in english_to_french_maximised:
                french_sentence = french_sentence + english_to_french_maximised[word] + " "
            else:
                print("word '"+ word +"' does not exist in trained language translation dictionary")
                continue
        return french_sentence
    
def test(sentences, choice):
    return tester(sentences,choice)
