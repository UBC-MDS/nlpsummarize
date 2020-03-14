import os
import nltk
import wget

def check_nltk_dependencies():
    """
    Checks the dependencies to use nltk package.

    If the necessary model is not present in the system, it is downloaded.
    """
    try:
        # Check if punkt has been downloaded or not, if not do so 
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            print('Downloading punkt...')
            nltk.download('punkt')
        
        # Check if stopwords has been downloaded or not, if not do so 
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            print('Downloading stopwords...')
            nltk.download('stopwords')

        # Check if averaged perceptron tagger has been downloaded or not, if not do so 
        try:
            nltk.data.find('taggers/averaged_perceptron_tagger')
        except LookupError:
            print('Downloading averaged_perceptron_tagger...')
            nltk.download('averaged_perceptron_tagger')
    except:
        print('Something went wrong when checking nltk dependencies')
        return False

    return True

def fasttext_dependencies():
    """
    Checks the dependencies to use fasttext package.

    If the necessary model is not present in the system, it is downloaded.
    """

    path = 'model/lid.176.bin'
    if not os.path.isfile(path): 
        try:
            print('Downloading fasttext pre-trained model')
              
            url = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin'
            wget.download(url, path)
        except:
            print('Something went wrong when downloading!!')
            return False
    return True

check_nltk_dependencies()
fasttext_dependencies()
