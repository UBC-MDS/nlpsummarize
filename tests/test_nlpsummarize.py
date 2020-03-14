
from nlpsummarize import nlp

import pandas as pd


def test_pos_english_input():
    """
    Test function to ensure that an English string is understood by the `get_part_of_speech` function.
    """
    true_results = pd.DataFrame({'adjective': 0.0741, 'noun': 0.2222, 'verb': 0.2963},index = [0])
    initial_df = nlp.NLPFrame({'text_col' : ['Today is a beautiful Monday and I would love getting a coffee. However, startbucks is closed.','It has been an amazing day today!']}, index = [0,1])

    b = ['adjective', 'noun', 'verb']
    res = initial_df.get_part_of_speech()
    a = list(res.columns)

    assert a==b , 'Default columns should be adjective, noun and verb'


def test_pos_chinese_input():
    """
    Test function to ensure that a Chinese string of text is understood by the `get_part_of_speech` function.
    """
    initial_df = nlp.NLPFrame({'text_col': ['彼は新しい仕事に本当に満足している']}, index = [0])
    res = initial_df.get_part_of_speech()
    b = ['adjective', 'noun', 'verb']
    a = list(res.columns)

    assert a==b, 'The function should return an output even for non-English text'


def test_pos_mixture_input():
    """
    Test function to ensure that the `get_part_of_speech` function can read different languages of strings.
    """
    initial_df = nlp.NLPFrame({'text_col': ['彼は新しい仕事に本当に満足している','It has been an amazing day today!']}, index = [0,1])
    res = initial_df.get_part_of_speech()
    b = ['adjective', 'noun', 'verb']
    a = list(res.columns)

    assert a==b, 'The function should return an output even for mixture of English and non-English sentences!'

def test_invalid_pos_input_1():
    """
    Test function to ensure that the `get_part_of_speech` function handles the input of multilingual values in pd Series.
    """
    initial_df = nlp.NLPFrame({'text_col': ['彼は新しい仕事に本当に満足している','It has been an amazing day today!']})
    try:
        res = initial_df.get_part_of_speech(show_only=5)
        assert False, 'The function should not be executed when the show only input is not an iterable object!!'
    except TypeError:
        pass

def test_polarity_input():
    """
    Test function to ensure that the `polarity` function properly classifies between "good" and "bad" text.
    """
    initial_df = nlp.NLPFrame({'text_col': ['he is a good guy','his behaviour is bad']}, index = [0,1])
    res = initial_df.polarity()
    b = ['positive_words', 'negative_words']
    a = list(res.columns)

    assert a==b, 'Default columns should be positive, negative'

def test_polarity_count():
    """
    Test function to ensure that the `polarity` function returns correct count values.
    """
    initial_df = nlp.NLPFrame({'text_col': ['sam is living a great life','he treats them so well']}, index = [0,1])
    res = initial_df.polarity()

    assert ((res.iloc[0,0] >= 0) & (res.iloc[0,1] >= 0)) , 'Count should be positive'

def test_df_summary_4():
    """
    Test function to ensure that the input data is in string format.
    """
    test_df = nlp.NLPFrame({'text_col' : ['Today is a great day \
                                and I wish I spent more time outside. I decided to go outside.\
                                English!']})
    input_data = test_df['text_col'][0]

    assert type(input_data) == str, 'The inputs are not strings'

def test_positive_summary_4():
    """
    Test function to ensure that the `summary_4` function is properly outputting a positive count.
    """
    initial_df = nlp.NLPFrame({'text_col': ['The coffee is good', 'I would like to have some']}, index = [0,1])
    res = initial_df.summary_4()

    assert ((res.iloc[0,0] >= 0) & (res.iloc[0,1] >= 0)) , 'Count should be positive'


def test_language_works():
    """
    Test function to ensure that the `detect_language` function is properly returning correct languages.
    """
    test_df = nlp.NLPFrame({'english_text' : ['I am a happy person'],
                        'mandarin_text': ['戰國策的版本存在非常多的錯誤'],
                        'spanish_text': ['Hola mi nombre es Bill y me gustan los gatos']
                       })

    assert test_df.detect_language(column = 'english_text' )['language'][0] == 'English', 'Incorrect Language'
    assert test_df.detect_language(column = 'mandarin_text')['language'][0] == 'Chinese', 'Incorrect Language'
    assert test_df.detect_language(column = 'spanish_text' )['language'][0] == 'Spanish', 'Incorrect Language'
