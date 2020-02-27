# author: Karanpal Singh
# date: 26 Feb 2020


def polarity(df):
    """
    This method will check and compute the polarity
    of the text data. This method will return:
            - Number of Positive words
            - Number of Negative words
            - Number of Neutral words
            
    -----------
    Arguments:
    df(Dataframe) : a pandas dataframe having textual data within it
    
    -----------
    Return:
    nop(integer): number of positive words
    nong(integer): number of negative words
    non(integer): number of neutral words
    
    -----------
    Example:
    >>>> df = pd.DataFrame({'text': 'He is a good guy. 
                                    This is the worst coffee I had in my life.'})
                                    
    >>>> polarity(df['text'])
     [1]  | positive words | negative words | neutral words |
          |         1      |           1    |    0          |
    ------------

    """
    
    
    
    

