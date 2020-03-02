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
    predictions = model.predict([text])
    x = predictions[0][0][0][-2:]
    language_name = languages.get(alpha_2=x).name
    return language_name


def test_language_textual(input_text):
    assert type(input_text) == str
