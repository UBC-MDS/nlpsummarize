# author: Samneet Chepal
# date: 26 Feb 2020

def detect_language(pd_df_col):
    '''
    This function will search through the Pandas DataFrame column of
    textual data to detect the language of the corpus.

    ------------
    Argument
        pd_df_col (pd.Series): column of Pandas Dataframe (i.e. Series)
                        containing text data.
    ------------
    Return
        string: type of language
    ------------
    Example
        >>> df = pd.DataFrame({'text_col' : ['I love travelling to Japan and
                                eating Mexican food but I can only speak
                                English!']})

        >>> detect_language(df['text_col'])
        [1]  'English'
    ------------
    '''
    pass
