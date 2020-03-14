# author: Samneet Chepal
# date: 26 Feb 2020
import pandas as pd
import fasttext
from pycountry import languages
import os

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

    path = 'model/lid.176.bin'
    if not os.path.isfile(path):
        try:
            print('Downloading fasttext pre-trained model')
              
            url = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin'
            wget.download(url, path)
        except:
            print('Something went wrong when downloading!!')
            return False

    pretrained_model_path = 'model/lid.176.bin'

    model = fasttext.load_model(pretrained_model_path)
    predictions = model.predict(pd_df_col)
    result = predictions[0][0][-2:]
    language = languages.get(alpha_2 = result)
    print(language.name)
    return language.name
