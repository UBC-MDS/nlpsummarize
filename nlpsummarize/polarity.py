# author: Karanpal Singh
# date: 26 Feb 2020

import pandas as pd
import re


def polarity(df_col):
    """
    This method will check and compute the polarity
    of the text data. This method will return:
            - Number of Positive words
            - Number of Negative words
            
    -----------
    Arguments:
    df_col (pd.DataFrame) : a column of pandas dataframe having textual data within it
    
    -----------
    Return:
    pd.DataFrame with columns number of positive and negative

    
    -----------
    Example:
    >>>> df = pd.DataFrame({'text': ['He is a good guy.
                                    This is the worst coffee I had in my life.']})
                                    
    >>>> polarity(df['text'])
     [1]  | positive words | negative words |
          |         1      |           1    |
    ------------

    """
    
    
    try:
        # loading positive lexicons
        positive_words = list(pd.read_csv('../data/positive-words.txt',skiprows=34, header = 'infer')['words'])
        
        # loading negative lexicons
        negative_words = list(pd.read_csv('../data/negative-words.txt',skiprows=34, header='infer')['words'])
    
    except:
        print('Error reading Lexicons. Please check if lexicon files are in data directory...')
    
    
    try:
    
        # concat messages for easy processing
        all_messages = df_col.str.cat(sep=', ')
        
    except:
        print('Concat failed, please provide valid column of textual data')
    
    
    try:
    
        # sensing tokens
        word_tokens = re.findall(r'\b\w[\w-]*\b', all_messages.lower())
        
    except:
        print('Tokenization failed, please provide a valid column of textual data')
    
    # counting positive words
    positive_word_count = 0
    for word in word_tokens:
        if word in positive_words:
            positive_word_count += 1
    
    # counting negative words
    negative_word_count = 0
    for word in word_tokens:
        if word in negative_words:
            negative_word_count += 1
            
    return pd.DataFrame({'positive_words':positive_word_count, 'negative_words':negative_word_count}, index = [0])
            
    
    
if __name__ == '__main__':
    df = pd.read_excel('../data/text_data.xlsx')
    print(polarity(df['text']))
    

