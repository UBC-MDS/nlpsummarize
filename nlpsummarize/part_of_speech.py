# author: Karlos Muradyan
# date: 26 Feb 2020

def get_part_of_speech(pd_df_col):
    '''
    This function generates statistics about the proportions of following
    parts of speech in the given column::
        - verbs
        - prepositions
        - adjectives
        - nouns
        - articles
    ------------
    Argument
        pd_df_col (pd.Series): column of pandas dataframe (i.e. Series)
                        containing text data.
    ------------
    Return
        pd.DataFrame with columns verbs, prepositions, adjectives, nouns, articles
    ------------
    Example
        >>> ex = pd.DataFrame({'text_col' : ['Today is a beautiful Monday
                                         and I would love getting a 
                                         coffee. However, startbucks 
                                         is closed.']})
        >>> get_part_of_speech(ex['text_col'])
        [1]  |   verbs    | prepositions | adjectives |   nouns   |  articles  |
             |    0.2     |     0.11     |     0.3    |    0.06   |     0.18   |
    ------------
    '''

    pass
