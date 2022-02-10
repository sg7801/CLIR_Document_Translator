# Cross Lingual Information Retrieval Document Translator

## Summary

*The **Cross Lingual Document Translator** is implemented by applying the **Information Retrieval** as **Statistical Machine Translation** by implementing **IBM Model 1**. We aim to translate the documents between **English and French** and calculate the **Cosine Similarity** and **Jaccard's Coefficient**.*

- IBM models are a series of models in increasing complexity, starting with lexical translation. IBM Model 1 is the simplest of such models. In IBM Model 1, sentence aligned bilingual corpora is used. We only consider the lexical translation of words. The end result is the word translation probabilities. 
- The expectation maximization algorithm helps us to investigate word translation probabilities if the word alignments are given and vice versa. This model takes all alignment probabilities equally likely. Alignments are taken care of by sucessors of IBM Model 1.

**If we assume that two requirements are completed**:
  - English Sentence **e**
  - Lexical Translation Probs **t(Foreign Word | English Word)**

Our next task would be to define a generative probability model that generates a foreign word for a given english word. 

**We follow the simple steps**:
- Pick a length for a foreign statement at random
- Pick the alignment function at random
- For each of the foreign position, we generate an foreign word by looking up the aligned English Words in alignment function and perform sampling on a foreign word from **t(. | e)**
- The whole process results in the foreign sentence, associated alignment probability **p(f,a | e)**

## Table of contents
- [Dataset](#dataset)
- [Expectation Maximization Algorithm](#em)
    - [Mathematical Implementation](#formula)
- [The pseudocode for IBM Model 1 and the EM Algorithm](#pseudo)
- [Flow of Control](#flow)
- [Implemented Modules](#module)
- [Running the Program](#program)
- [Resultant Calculations](#calc)
- [Future Improvements](#future)
 
## Dataset <a name="dataset"></a>

The dataset used for this project is a **bilingual text corpora** named **Europarl**. The Europarl parallel corpus is extracted from the proceedings of the European Parliament. The french-english corpus had around **2008050** french lines and **2007938** english lines of which a subset of **80,000** lines were chosen for training our model. The chosen dataset was divided into into training set for training the model and the test sets for testing the model. 

## Expectation Maximization Algorithm <a name="em"></a>

***The EM Algorithm helps us to maximize the likelihood of the given function. When we assume that the given dataset is derived from the mixture of multiple model with their own set of specific parameters then we assume some value for all parameters.*** 

- The EM Algorithm has been implemented in the IBM Model 1. The algorithm uses the observable samples of latent variables and predicts the values of observable samples. The model calculates and store the probabilites of each and every word of one language being direct translation to some word in other language. 

- The IBM Model first goes through the corpus. It creates the list of all words in the language where the matrix gets created and each cell **(a, b)** consists of the probability of word **a** being the translation of word **b**. The model generates all possible alignments and calculates the probabilities. 
 
- We start with the initialization step by initializing the parameters with initial set of values. The Expectation Maximization Algorithm calculates the **Local Maximum Likelihood (MLE)** parameters for latent variables in statistical model. It calculates the probability of the object belonging to a particular model. This takes place for all models.

- The Expectation step estimates or guesses the values of missing or incomplete data. It updates all the variables.

- Then, this step is followed by maximization step, where it recalculates the parameters of each model by maximizing the likelihood. The final results provides us the clusters where each belongs to the particular model of known parameters. 

- These steps can be repeated for number of iterations till the **convergence** occurs.

**The EM Algorithm in nutshell is used to** : 
  - Initialize model parameters
  - Assign probabilities to the missing data
  - Estimate the model parameters from the completed data
  - Iterate

## Mathematical Implementation <a name="formula"></a>
*Below formula calculates the translation probability where **e** represents the english sentence, **f** represents the foreign sentence with an alignment of each word e to f according to the alignment function. The epsilon represents the normalization constant.* 

![image](https://user-images.githubusercontent.com/61888364/131600469-e56f05f5-3ced-473f-96d3-22567dfe018a.png)

- **We took french as foreign language hence f represents the french sentence. To compute the p(a | e,f) we will apply the chain rule and get below formula** : 

![image](https://user-images.githubusercontent.com/61888364/131601540-85eea59e-44e1-444a-92dc-1620d738cbaa.png)

- **Now, we already have the formula for p(e,a | d) ,we need to compute p(e|d). We get** :

![image](https://user-images.githubusercontent.com/61888364/131601752-53509c8e-b88d-4ac5-a10f-e4855818bfcd.png)

- **The last step made the IBM Model 1 estimation tractable**.
![image](https://user-images.githubusercontent.com/61888364/131601788-d9261850-549f-4f41-a7ab-309279390bda.png)

- **Upon combining what we have we get**:

![image](https://user-images.githubusercontent.com/61888364/131601932-8ddd39c5-70f4-4e2b-b570-19e90bdfbfc8.png)

- **Now we will collect counts from each sentence pair e, f for each word pair e and f.** 
![image](https://user-images.githubusercontent.com/61888364/131602040-8b46d14c-0dfa-4050-9386-9fad727915bc.png)
![image](https://user-images.githubusercontent.com/61888364/131602092-51efc6b7-5a58-47ce-96ae-bca29159909c.png)

- **After collecting counts over the corpus we estimate the model** :

![image](https://user-images.githubusercontent.com/61888364/131602145-66ab2d9e-8927-4681-bcc0-d660c097d632.png)

## The pseudocode for IBM Model 1 and the EM Algorithm :<a name="pseudo"></a>
*(Here **e** represents the **English** language and **f** represents the **French** language)*

```
Input : set of sentence pairs (e,d)       14.     //collect counts
Output: translation prob t(e|d)           15.     for all words e in e do
  1. initialize t(e|f) uniformly          16.       for all words f in f do
  2. while not converged do               17.         count(e|f) += (t(e|f)/s-total(e))
  3. //initialize                         18.         total(f) += (t(e|f)/s-total(e))
  4. count(e|f) = 0 for all e,f           19.       end for
  5. total(f) = 0 for all f               20.     end for
  6. for all sentence pairs(e, f) do      21.   end for
  7.  //compute normalization             22.   //estimate probabilities
  8.  for all words e in e do             23.   for all foreign words f do
  9.    s-total(e) = 0                    24.     for all English words e do
 10.    for all words f in f do           25.       t(e|f) = count(e|f)/total(f)
 11.      s-total(e) += t(e|f)            26.      end for
 12.    end for                           27.     end for
 13.  end for                             28.   end while  
```
## Flow of Control <a name="flow"></a>
![Flow Chart](https://user-images.githubusercontent.com/61888364/131933335-cd79851c-dd15-4412-a943-0aecd77555ab.png)

## Implemented Modules <a name="module"></a>

*Multiple modules have been implemented for the project. Their functionality descriptions are as follows :* 

- **main.py** : This file is the central control for our entire project. It controls the execution of all other modules. We can run this file in command prompt by using **python main.py** command and choose from given options to perform various training and testing operations.

- **Training.py** : This module contains the **Information Retrieval model**. This module will train the model using two major functions :
  - **tokenize_sentences(sentences, index)** : This function take two parameters - sentences which denotes the sentences and index that denotes the maximum words that can be present in the sentence. It will tokenize and return the words from the sentences.
  - **model_trainer()** : This function trains our IBM model.

- **Testing** : This module tests the sentences by translating them to second language. User enters the sentence and based on their entered choice of language the sentence gets translated.

- **IBM_Model1_EM.py** :
This module will implement the IBM Model 1 for language translation. It has two major functions:
  - **expectation_maximization(french_word_dict, english_word_dict, french_sentences, english_sentences)** : This function is used to populate the e/f matrix according to IBM Model 1 algorithm.
  - **get_translation_probability(english, foreign, total, english_dict, foreign_dict)**: This function returns the probability of the sentence one one language to be translated to the sentence of other language.

- **English_To_French.py** : This module implements the final translation of English sentence to French sentence. It contains two functions:
  -  **sen_tokenizer(list_of_sentences)** : This function will take the input sentence via  **list_of_sentences** parameter and returns the tokenized list of words of that sentence.
  -  **english_to_french()** : This function translates the sentence from English to French. The input is taken from already created input.txt from Dataset Folder and the output is stored in already created output.txt in Dataset folder.

- **French_To_English.py** : This module implements the translation of French sentences to English sentences. Two functions have been used in this module :
  - **sen_tokenizer(list_of_sentences)** : This function will take the input sentence via  **list_of_sentences** parameter and returns the tokenized list of words of that sentence.
  -  **french_to_english()** : This function translates the sentence from French to English. The input is taken from already created input.txt from Dataset Folder and the output is stored in already created output.txt in Dataset folder.

- **Cosine_Similarity.py** : This module implements the cosine similarity calculation between two sentences. It has one function :
  - **cosine(string1)** : This function will calculate and display the cosine similarity between the translated sentence taken from output.txt file from Dataset Folder and actual sentence taken from the actual.txt taken from the Dataset folder. Average cosine similarity would be returned.

- **Jaccard_Coefficient.py** : This module implements the Jaccard Coefficient calculation between two sentences. It has one function : 
  -  **jaccard_coeff(string1)** : This function will calculate and display the jaccard coefficient between the translated sentence taken from output.txt file from Dataset Folder and actual sentence taken from the actual.txt taken from the Dataset folder. Average Jaccard coefficient would be returned.

- **Utility.py** : This module has one function **convergence(second, first, number_of_iterations)** that implements and returns boolean result by checking if the probabilities in the e|f matrix have converged or not after **200** iterations.

## Running the Program : <a name="program"></a>

*The program starts with **main.py** module. Users can run it in the command prompt by typing **python main.py** command. **nltk.stopwords** and **nltk.punkt** must be pre-installed in the python environment. This would show a list of options on the screen. They would be :*

1. **Train the Model**
2. **Test the sentence to translate**
3. **Translate a document**
4. **Calculate Cosine Similarity**
5. **Calculate Jaccard coefficient**
6. **Exit**

Depending upon the choice of user they can perform multiple operations. 
- **Option 1** would train the IBM Model for translation between French and English
- **Option 2** would Test the translation model. User would enter the choice of language followed by the sentence to be translated. The output would be the translated sentence.
- **Option 3** would translate the entire test document from the Dataset folder between French to English depending upon the choice entered and the output would be stored in output.txt file in Dataset folder.
- **Option 4** would calculate the cosine similarity between the translated document from output.txt from the Dataset document and the actual document actual.txt from the Dataset document.
- **Option 5** would calculate the Jaccard Coefficient between the translated document from output.txt from the Dataset document and the actual document actual.txt from the Dataset document.
- **Option 6** exists the user from the console.

## Resultant Calculations : <a name="calc"></a>

*We compared the similarity between the actual translation and the output translations of our IBM Model. The sentences are compared one at a time and the performed calculations are averaged. Below are the obtained results after **200 iterations**:*

| Cosine Similarity   |    0.089   |
| ------------------- | ----------- |
| **Jaccard Coefficient** |    **0.059**   |

## Future Improvements <a name = "future"></a>
- Out of around **2 million** aligned sentences only **80,000** were chosen for training the model. We could increase the size of corpus in future to increase the accuracy.
- The length of the sentences has to be limited by considering only those with less than **51 words**. It decreased the dictionary size and hence some words could not be found while translating. This could be improved by considering more words in a sentence after increasing computational powers.
- The position of words in the source and target sentences are independent. This generates wrong outputs when a contiguous phrase is translated.
- Since IBM Model 1 focuses on lexical alignments, the target words can have at most one corresponding word in source language. This generates wrong outputs in scenarios where a phrase in source sentence translates to a single word in target sentence.
- The IBM Model 1 only provided the lexical translations and ignores the alignments. This could be improved by using successors of IBM Model 1.
- The major drawback is that it can produce same source word for multiple target words.
- There were lack of some sufficient alignments of target words due to its lexical alignment nature.
