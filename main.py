import Cosine_Similarity
import Utility
import Testing 
import Training 
import Jaccard_Coefficient
import IBM_Model1_EM
import French_To_English
import English_To_French
import nltk
nltk.download('punkt')

while True:
    try:
        choice = int(input('\n\nEnter your choice of action: \n\t1: Train the Model\n\t2: Test sentence to translate\n\t3: Translate a document \n\t4: Calculate Cosine Similarity \n\t5: Calculate Jaccard coefficient \n\t6: Exit\n'))
    except ValueError:
        print ("Not a number")
    
    if choice == 1:
        Training.model_trainer()
    elif choice == 2:
        try:
            translate_choice = int(input('Select Translation Choice: \n\t1: French to English \n\t2: English to French\n'))
        
        except ValueError:
            print ("Not a number")
        
        if translate_choice > 2 or translate_choice < 1 :
            print("Invalid Option")
            exit()
        
        sentence_to_translate = input("Please provide sentence to translate: ")
        translated_sentence = Testing.test(sentence_to_translate,translate_choice)
        print(translated_sentence)
        
    elif choice == 3:
        try:
            translate_choice = int(input('Select Translation Choice: \n\t1: French to English \n\t2: English to French\n'))
        
        except ValueError:
            print ("Not a number")
        
        if translate_choice > 2 or translate_choice < 1 :
            print("Invalid Option")
            exit()
        if translate_choice == 1:
            French_To_English.french_to_english()
        elif translate_choice == 2:
            English_To_French.english_to_french()

    elif choice == 4:
        try:
            language = int(input('\n\nPlease choose the language of output and actual documents \n\t1: French\n\t2: English\n'))
        except ValueError:
            print ("Not a number")

        if language > 2 or language < 1 :
            print("Invalid Option")
            exit()
            
        Cosine_Similarity.cosine(language)
        
    elif choice == 5:
        try:
            language = int(input('\n\nPlease choose the language of output and actual documents \n\t1: French\n\t2: English\n'))
        except ValueError:
            print ("Not a number")

        if language > 2 or language < 1 :
            print("Invalid Option")
            exit()
            
        Jaccard_Coefficient.jaccard_coeff(language)
        
    elif choice == 6:
        print("Thank you for your visit!")
        break
    else:
        print("invalid mode")
