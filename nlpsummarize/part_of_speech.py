# author: Karlos Muradyan
# date: 26 Feb 2020

import nltk
import pandas as pd


def get_part_of_speech(pd_df_col, show_only=['adjective', 'noun', 'verb']):
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
        show_only (list-like): names of the part of speech of put into the final result.
            If False or None, all part of speech will be shown (i.e. ['adjective', 'adposition',
            'adverb', 'conjuction', 'article', 'noun', 'numeral', 'particle', 'pronoun', 'verb',
            'punctuation']). Default: ['adjective', 'noun', 'verb'].
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
    # Adding initial check of the input
    if type(pd_df_col) != pd.core.series.Series:
        raise TypeError('pd_df_col should be column of a dataframe, i.e. pd.core.series.Series type')


    # Defining mapping of abbreviation to the actual part of speech name.
    lookup_dict = {'ADJ': 'adjective',
                   'ADP': 'adposition',
                   'ADV': 'adverb',
                   'CONJ': 'conjuction',
                   'DET': 'article',
                   'NOUN': 'noun',
                   'NUM': 'numeral',
                   'PRT': 'particle',
                   'PRON': 'pronoun',
                   'VERB': 'verb',
                   '.': 'punctuation'}

    # Selecting subset of the part of speech that is interesting to the user
    try:
        if show_only:
            lookup_dict = {k: v for k, v in lookup_dict.items() if v in show_only}
    except TypeError:
        raise TypeError('show_only should be iterable object containing values from part of speech')

    try:
        concatenated_text = '\n'.join(pd_df_col)
        concatenated_text = nltk.word_tokenize(concatenated_text)
        tags = nltk.pos_tag(concatenated_text, tagset='universal')
    except LookupError as e:
        print("If you haven't done so, please before running get_part_of_speech\
                function please run:\n\n>>> nltk.download('punkt')\
                \n>>> nltk.download('averaged_perceptron_tagger')\n\
                >>> nltk.download('universal_tagset')")
        return None

    # Counting part of speech and getting proportions
    counts = {k: 0 for k in lookup_dict.keys()}
    for word in tags:
        if word[1] in counts:
            counts[word[1]] += 1

    counts = {lookup_dict[k]: round(v/len(tags), 4) for k, v in counts.items()}
    return pd.DataFrame(counts, index=[0])


if __name__ == '__main__':
    # ex = pd.DataFrame({'text_col' : ['Today is a beautiful Monday and I would love getting a coffee. However, startbucks is closed.','It has been an amazing day today!']})
    # print(get_part_of_speech(ex['text_col']))
        
    ex2 = pd.DataFrame({'text_col': ['彼は新しい仕事に本当に満足している','It has been an amazing day today!']})
    print(get_part_of_speech(ex2['text_col']))
