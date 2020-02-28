# author: Karanpal Singh
# date: 26 Feb 2020


def polarity(df_col):
    """
    This method will check and compute the polarity
    of the text data. This method will return:
            - Number of Positive words
            - Number of Negative words
            - Number of Neutral words
            
    -----------
    Arguments:
    df_col (pd.DataFrame) : a column of pandas dataframe having textual data within it
    
    -----------
    Return:
    pd.DataFrame with columns number of positive, negative and neutral words

    
    -----------
    Example:
    >>>> df = pd.DataFrame({'text': ['He is a good guy.
                                    This is the worst coffee I had in my life.']})
                                    
    >>>> polarity(df['text'])
     [1]  | positive words | negative words | neutral words |
          |         1      |           1    |    0          |
    ------------

    """
    
    
    
    

