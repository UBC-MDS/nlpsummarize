### Function authored by Vignesh Chandrasekaran

def summary_4_sentence_stopwords_freq_detection(pd_df_col):
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
        nos (integer)      : number of sentences present in a column of the dataframe
        nosw (integer)     : number of stop-words present in a column of the dataframe
        list_hf (integer)  : list of top 5 frequetly encountered words
        hf (integer)       : number of times the high frequency word was encountered.
    
    ------------
    Example
        >>> ex = pd.DataFrame({'text_col' : 'Today is a beautiful Monday
                                         and I would love getting a 
                                         coffee. However, startbucks 
                                         is closed.'})
        
        >>> summary_4(ex['text_col'])
        
        [1]  | number of sentences | number of stop words | high freq. words |
             |         2           |           6          |    is(2), a(2)   |    
    ------------
    
    '''




