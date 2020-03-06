# author: Samneet Chepal
# date: 26 Feb 2020
import pandas as pd
import fasttext
import pycountry
from pycountry import languages

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
    pretrained_model_path = '/tmp/lid.176.bin'
    model = fasttext.load_model(pretrained_model_path)
    predictions = model.predict(pd_df_col)
    result = predictions[0][0][-2:]
    language = languages.get(alpha_2 = result)
    print(language.name)
    return language.name


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
