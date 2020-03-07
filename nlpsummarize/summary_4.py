# Author : Vignesh Chandrasekaran 
# Date : 26-Feb-2020

import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize
import pandas as pd
from nltk.corpus import stopwords

from itertools import islice

def summary_4(pd_df_col, nof=3):
    '''
    This function generates the following:
        - number of sentences, 
        - number of stop words
        - list of high frequency 
        - frequency of the words
    when a column of a pandas dataframe is passed in.  
    ------------
    Argument
        pd_df_col (array): pandas dataframe with a columns having characters
    
    ------------
    Return
        dataframe  with the following elements:
        nos       : number of sentences present in a column of the dataframe
        nosw      : number of stop-words present in a column of the dataframe
        list_hf   : list of top 5 frequetly encountered words
        hf        : number of times the high frequency word was encountered.
    
    ------------
    Example
        >>> ex = pd.DataFrame({'text_col' : ['Today is a beautiful Monday
                                         and I would love getting a 
                                         coffee. However, startbucks 
                                         is closed.']})
        
        >>> sentence_stopwords_freq_detection(ex['text_col'])
        
        [1]  | number of sentences | number of stop words | high freq. words |
             |         2           |           6          |    is(2), a(2)   |    
    ------------
    
    '''
    
    #Concatenate all the sentences. Defaults a '.' when going from one row to another.
    all_messages = df['text'].str.cat(sep='. ')
    
    #Computes the number of sentences
    number_of_sentences = len(sent_tokenize(all_messages))
    
    #Computes number of stop words
    stop = len(stopwords.words('english'))
    
    #Splits the entire paragraph into individual words
    word_list = all_messages.split()
    wordfreq = []
    for w in word_list:
        wordfreq.append(word_list.count(w))    
    wordfreq_pair = dict((list(zip(word_list, wordfreq))))
    
    #Sorts the dictionary by frequency.
    aux = [(wordfreq_pair[key], key) for key in wordfreq_pair]
    aux.sort()
    aux.reverse()
    
    #Extracts the first nof number of words
    freq = aux[0:nof]
    
    #Returns a pandas dataframe
    return pd.DataFrame({ 'Number of sentences' : number_of_sentences,
                         'Stop words' : stop, 
                         'Frequency' : [freq]})


df = pd.read_excel('../data/text_data.xlsx')
summary_4(df['text'])