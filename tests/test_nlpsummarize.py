
from nlpsummarize import nlp

import pandas as pd

def test_init_1():
    """
    Test initialization of the class NLPFrame
    """

    initial_df = nlp.NLPFrame({'text_col' : ['Today is a beautiful Monday and I would love getting a coffee. However, startbucks is closed.','It has been an amazing day today!']}, index = [0,1])

    assert initial_df.column == 'text_col'


def test_init_2():
    """
    Test initialization of the class NLPFrame
    """

    initial_df = nlp.NLPFrame({'text_col' : ['Today is a beautiful Monday and I would love getting a coffee. However, startbucks is closed.','It has been an amazing day today!']}, index = [0,1], column = 'non_existing')
    assert initial_df.column == 'text_col'

def test_init_3():
    """
    Test initialization of the class NLPFrame that doesn't have text column
    """

    initial_df = nlp.NLPFrame({'text_col' : [5,6,8]})
    assert initial_df.column == None

def test_get_nlp_summary_1():
    """
    Tests get_nlp_summary function for NLPFrame without column with text
    """

    initial_df = nlp.NLPFrame({'text_col' : [5,6,8]})
    try:
        initial_df.get_nlp_summary()
        assert False
    except ValueError:
        pass
    
def test_get_nlp_summary_2():
    """
    Tests get_nlp_summary function for NLPFrame with wrong column specified
    """

    initial_df = nlp.NLPFrame({'text_col' : ['Today is a beautiful Monday and I would love getting a coffee. However, startbucks is closed.','It has been an amazing day today!']}, index = [0,1], column = 'non_existing')
    res = initial_df.get_nlp_summary(column = 'non_existing')
    assert res.equals(pd.DataFrame())

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

def test_pos_output_columns():
    """
    Test function to ensure that the `get_part_of_speech` function outputs the POS that are given as input
    """

    initial_df = nlp.NLPFrame({'text_col': ['彼は新しい仕事に本当に満足している','It has been an amazing day today!']}, index = [0,1])
    res = initial_df.get_part_of_speech(show_only=False)
    a = len(res.columns)

    assert a>0, 'The function should return an output even for mixture of English and non-English sentences!'

def test_pos_output_columns_2():
    """
    Test function to ensure that the `get_part_of_speech` function error handling
    """

    initial_df = nlp.NLPFrame({'text_col': ['彼は新しい仕事に本当に満足している','It has been an amazing day today!']}, index = [0,1])
    try:
        res = initial_df.get_part_of_speech(show_only=5)
        assert False, 'The function should throw an error when show_only argument is not valid'
    except TypeError:
        pass

def test_pos_output_columns_3():
    """
    Test function to ensure that the `get_part_of_speech` function error handling
    """

    initial_df = nlp.NLPFrame({'text_col' : [5,6,8]})
    try:
        initial_df.get_part_of_speech()
        assert False
    except ValueError:
        pass

def test_pos_invalid_input_4():
    """
    Tests get_pos function for NLPFrame with wrong column specified
    """

    initial_df = nlp.NLPFrame({'text_col' : ['Today is a beautiful Monday and I would love getting a coffee. However, startbucks is closed.','It has been an amazing day today!']}, index = [0,1], column = 'non_existing')
    try:
        initial_df.get_part_of_speech(column = 'non_existing')
        assert False
    except ValueError:
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

def test_polarity_1():
    """
    Tests polarity function for NLPFrame without column with text
    """

    initial_df = nlp.NLPFrame({'text_col' : [5,6,8]})
    try:
        initial_df.polarity()
        assert False
    except ValueError:
        pass
    
def test_polarity_2():
    """
    Tests polarity function for NLPFrame with wrong column specified
    """

    initial_df = nlp.NLPFrame({'text_col' : ['Today is a beautiful Monday and I would love getting a coffee. However, startbucks is closed.','It has been an amazing day today!']}, index = [0,1], column = 'non_existing')
    try:
        res = initial_df.polarity(column = 'non_existing')
        assert False
    except ValueError:
        pass

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

def test_summary4_1():
    """
    Tests summary_4 function for NLPFrame without column with text
    """

    initial_df = nlp.NLPFrame({'text_col' : [5,6,8]})
    try:
        initial_df.summary_4()
        assert False
    except ValueError:
        pass
    
def test_summary4_2():
    """
    Tests summary_4 function for NLPFrame with wrong column specified
    """

    initial_df = nlp.NLPFrame({'text_col' : ['Today is a beautiful Monday and I would love getting a coffee. However, startbucks is closed.','It has been an amazing day today!']}, index = [0,1], column = 'non_existing')
    try:
        res = initial_df.summary_4(column = 'non_existing')
        assert False
    except ValueError:
        pass

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


def test_language_1():
    """
    Tests detect_language function for NLPFrame without column with text
    """

    initial_df = nlp.NLPFrame({'text_col' : [5,6,8]})
    try:
        initial_df.detect_language()
        assert False
    except ValueError:
        pass

def test_language_2():
    """
    Tests detect_language function for NLPFrame with wrong column specified
    """

    initial_df = nlp.NLPFrame({'text_col' : ['Today is a beautiful Monday and I would love getting a coffee. However, startbucks is closed.','It has been an amazing day today!']}, index = [0,1], column = 'non_existing')
    try:
        initial_df.detect_language(column = 'non_existing')
        assert False
    except ValueError:
        pass

def test_read_csv_1():
    """
    Testing read_csv file
    """

    res = nlp.read_csv('./data/sample_csv.csv')

    assert type(res) == nlp.NLPFrame

def test_read_csv_2():
    """
    Testing invalid input
    """

    try:
        nlp.read_csv('non_existing.file')
        assert False
    except ValueError:
        pass

def test_read_excel_1():
    """
    Testing read_excel file
    """

    res = nlp.read_excel('./data/text_data.xlsx')

    assert type(res) == nlp.NLPFrame


def test_read_excel_2():
    """
    Testing invalid input
    """

    try:
        nlp.read_csv('non_existing.file')
        assert False
    except ValueError:
        pass
