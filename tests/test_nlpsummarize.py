from nlpsummarize.part_of_speech import get_part_of_speech
from nlpsummarize.polarity import polarity
from nlpsummarize.detect_language import detect_language
import pandas as pd


def test_english_input():
    true_results = pd.DataFrame({'adjective': 0.0741, 'noun': 0.2222, 'verb': 0.2963},index = [0])
    initial_df = pd.DataFrame({'text_col' : ['Today is a beautiful Monday and I would love getting a coffee. However, startbucks is closed.','It has been an amazing day today!']}, index = [0,1])

    b = ['adjective', 'noun', 'verb']
    res = get_part_of_speech(initial_df['text_col'])
    a = list(res.columns)

    assert a==b , 'Default columns should be adjective, noun and verb'


def test_chinese_input():
    initial_df = pd.DataFrame({'text_col': ['彼は新しい仕事に本当に満足している']}, index = [0])
    res = get_part_of_speech(initial_df['text_col'])
    b = ['adjective', 'noun', 'verb']
    a = list(res.columns)

    assert a==b, 'The function should return an output even for non-English text'


def test_mixture_input():
    initial_df = pd.DataFrame({'text_col': ['彼は新しい仕事に本当に満足している','It has been an amazing day today!']}, index = [0,1])
    res = get_part_of_speech(initial_df['text_col'])
    b = ['adjective', 'noun', 'verb']
    a = list(res.columns)

    assert a==b, 'The function should return an output even for mixture of English and non-English sentences!'

def test_polarity_input():
    initial_df = pd.DataFrame({'text_col': ['he is a good guy','his behaviour is bad']}, index = [0,1])
    res = polarity(initial_df['text_col'])
    b = ['positive_words', 'negative_words']
    a = list(res.columns)

    assert a==b, 'Default columns should be positive, negative'

def test_polarity_count():
    initial_df = pd.DataFrame({'text_col': ['sam is living a great life','he treats them so well']}, index = [0,1])
    res = polarity(initial_df['text_col'])

    assert ((res.iloc[0,0] >= 0) & (res.iloc[0,1] >= 0)) , 'Count should be positive'

def test_language_textual():
    test_df = pd.DataFrame({'text_col' : ['I love travelling to Japan and \
                                eating Mexican food but I can only speak \
                                English!']})
    input_data = test_df['text_col'][0]

    assert type(input_data) == str, 'The function input should be in a string format'


def test_language_works():
    test_df = pd.DataFrame({'english_text' : ['I am a happy person'],
                        'mandarin_text': ['戰國策的版本存在非常多的錯誤'],
                        'spanish_text': ['Hola mi nombre es Bill y me gustan los gatos']
                       })

    assert detect_language(test_df['english_text'][0]) == 'English', 'Incorrect Language'
    assert detect_language(test_df['mandarin_text'][0]) == 'Chinese', 'Incorrect Language'
    assert detect_language(test_df['spanish_text'][0]) == 'Spanish', 'Incorrect Language'


