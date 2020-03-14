# authors: Samneet Chepal, Karlos Muradyan, Karanpal Singh, Vignesh Chandrasekaran 
# date: 26 Feb 2020

import pandas as pd
import nltk
import fasttext
from pycountry import languages
import re
from nltk.tokenize import sent_tokenize
import pandas as pd
from nltk.corpus import stopwords
from itertools import islice
import wget
import os

class NLPFrame(pd.DataFrame):
    """
    This class implements the extension of pandas DataFrame to give summary of a column
    containing text.
    """
    def __init__(self, data = None, column = None, *args, **kwargs):
        """
        Initializing NLPFrame.

        Parameters
        ----------
        data: ndarray (structured or homogeneous), Iterable, dict, or DataFrame
            Dict can contain Series, arrays, constants, or list-like objects.

        column: string or None
            The column name that will be used as default when doing summary. If None,
            the column is seleted automatically.

        *args:
            Other arguments that are passed to pd.DataFrame during initialization

        **kwargs:
            keyword arguments to pass pd.DataFrame during initialization
        """
        super(NLPFrame, self).__init__(data, *args, **kwargs)

        # For now, we support only one column
        self.column = column if column else self.select_dtypes(include='object').columns[0]

    def check_nltk_dependencies(self):
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

    def fasttext_dependencies(self):
        """
        Checks the dependencies to use fasttext package.

        If the necessary model is not present in the system, it is downloaded.
        """

        path = './model/lid.176.bin'
        if not os.path.isfile(path): 
            try:
                print('Downloading fasttext pre-trained model')
                  
                url = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin'
                wget.download(url, path)
            except:
                print('Something went wrong when downloading!!')
                return False
        return True

    def get_nlp_summary(self, column = ''):
        """
        Generates full summary of the column specified or one that was picked automatically.

        -------------
        Parameters
            column(string):
                If specified, it will be used when generating summary. If it is an empty string,
                the default one will be used

        ------------
        Return
            nlp.NLPFrame: contains full summary of the column.

        -----------
        Example

        >>> ex = nlp.NLPFrame({'text_col' : ['Today is a beautiful Monday\
                                             and I would love getting a \
                                             coffee. However, startbucks\
                                             is closed.']})

        [0]    language  Number of sentences  Stop words                      Frequency  adjective    noun    verb  positive_words  negative_words
            0  English                    2         179  [(2, is), (2, a), (1, would)]     0.0526  0.2105  0.3158               2               0

        """
        column = column if column else self.column

        if not self.check_nltk_dependencies() or not self.fasttext_dependencies():
            print('Dependencies are not met. Please read the instructions or contact the developers for further details')
            return None

        try:
            res = pd.concat((
                self.detect_language(column=column),
                self.summary_4(column=column),
                self.get_part_of_speech(column=column),
                self.polarity(column=column)), axis=1)
        except ValueError:
            print(f"The column {column} doesn't exist")
            res = NLPFrame()

        return res

    def summary_4(self, nof=3, column = ''):
        '''
        This function generates the following:
            - number of sentences, 
            - number of stop words
            - list of high frequency 
            - frequency of the words
        when a column of a pandas dataframe is passed in.  
        ------------
        Argument
            nof (int): number of Top nof to extract.
            column (string): Column to generate summary from. If empty string, 
                the default is taken.
            
        ------------
        Return
            dataframe  with the following elements:
            nos       : number of sentences present in a column of the dataframe
            nosw      : number of stop-words present in a column of the dataframe
            list_hf   : list of top 5 frequetly encountered words
            hf        : number of times the high frequency word was encountered.
        
        ------------
        Example
            >>> ex = nlp.NLPFrame({'text_col' : ['Today is a beautiful Monday
                                             and I would love getting a 
                                             coffee. However, startbucks 
                                             is closed.']})
            
            >>> ex.sentence_stopwords_freq_detection()
            
            [1]  | number of sentences | number of stop words | high freq. words |
                 |         2           |           6          |    is(2), a(2)   |    
        ------------
        
        '''
        column = column if column else self.column
        
        try:
            pd_df_col = self.__getitem__(column)
        except KeyError:
            raise ValueError(f"The column {column} doesn't exist in the NLPFrame")
        
        #Concatenate all the sentences. Defaults a '.' when going from one row to another.
        all_messages = pd_df_col.str.cat(sep='. ')
        
        #Computes the number of sentences
        number_of_sentences = len(sent_tokenize(all_messages))
        
        #Computes number of stop words
        stop = len(stopwords.words('english'))
        
        #Splits the entire paragraph into individual words
        word_list = all_messages.split()
        wordfreq = []
        for w in word_list:
            wordfreq.append(word_list.count(w))    
        wordfreq_pair = dict((list(zip(word_list, wordfreq))))
        
        #Sorts the dictionary by frequency.
        aux = [(wordfreq_pair[key], key) for key in wordfreq_pair]
        aux.sort()
        aux.reverse()
        
        #Extracts the first nof number of words
        freq = aux[0:nof]
        
        #Returns a pandas dataframe
        return pd.DataFrame({ 'Number of sentences' : number_of_sentences,
                             'Stop words' : stop, 
                             'Frequency' : [freq]})



    def get_part_of_speech(self, show_only=['adjective', 'noun', 'verb'], column=''):
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
            show_only (list-like): names of the part of speech of put into the final result.
                If False or None, all part of speech will be shown (i.e. ['adjective', 'adposition',
                'adverb', 'conjuction', 'article', 'noun', 'numeral', 'particle', 'pronoun', 'verb',
                'punctuation']). Default: ['adjective', 'noun', 'verb'].
            column(string):
                If specified, it will be used when generating summary. If it is an empty string,
                the default one will be used
        ------------
        Return
            pd.DataFrame with columns verbs, prepositions, adjectives, nouns, articles
        ------------
        Example
            >>> ex = nlp.NLPFrame({'text_col' : ['Today is a beautiful Monday
                                             and I would love getting a 
                                             coffee. However, startbucks 
                                             is closed.']})
            >>> ex.get_part_of_speech()
            [1]  |   verbs    | prepositions | adjectives |   nouns   |  articles  |
                 |    0.2     |     0.11     |     0.3    |    0.06   |     0.18   |
        ------------
        '''
        # Adding initial check of the input
#         if type(pd_df_col) != pd.core.series.Series:
#             raise TypeError('pd_df_col should be column of a dataframe, i.e. pd.core.series.Series type')
# 
        column = column if column else self.column
        try:
            pd_df_col = self.__getitem__(column)
        except KeyError:
            raise ValueError(f"The column {column} doesn't exist in the NLPFrame")

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

    def detect_language(self, column = ''):
        '''
        This function will search through the Pandas DataFrame column of
        textual data to detect the language of the corpus.

        ------------
        Argument
            column(string):
                If specified, it will be used when generating summary. If it is an empty string,
                the default one will be used
        ------------
        Return
            pd.DataFrame: contains one column having information about the language
        ------------
        Example
            >>> df = nlp.NLPFrame({'text_col' : ['I love travelling to Japan and
                                    eating Mexican food but I can only speak
                                    English!']})

            >>> df.detect_language()
            

            [1]   language
               0  English

        ------------
        '''
        column = column if column else self.column
        try:
            pd_df_col = self.__getitem__(column)
        except KeyError:
            raise ValueError(f"The column {column} doesn't exist in the NLPFrame")
        
        
        pretrained_model_path = 'model/lid.176.bin'
        model = fasttext.load_model(pretrained_model_path)
        predictions = model.predict(''.join(pd_df_col))
        result = predictions[0][0][-2:]
        language = languages.get(alpha_2 = result)
        return pd.DataFrame({'language': [language.name]})

    def polarity(self, column=''):
        """
        This method will check and compute the polarity
        of the text data. This method will return:
                - Number of Positive words
                - Number of Negative words
                
        -----------
        Arguments:
            column(string):
                If specified, it will be used when generating summary. If it is an empty string,
                the default one will be used
        
        -----------
        Return:
        pd.DataFrame with columns number of positive and negative

        
        -----------
        Example:
        >>>> df = nlp.NLPFrame({'text': ['He is a good guy.
                                        This is the worst coffee I had in my life.']})
                                        
        >>>> df.polarity(df['text'])
         [1]  | positive words | negative words |
              |         1      |           1    |
        ------------

        """
        
        
        column = column if column else self.column
        try:
            pd_col = self.__getitem__(column)
        except KeyError:
            raise ValueError(f"The column {column} doesn't exist in the NLPFrame")
        
        
        try:
            # loading positive lexicons
            positive_words = list(pd.read_csv('data/positive-words.txt',skiprows=34, header = 'infer')['words'])
            
            # loading negative lexicons
            negative_words = list(pd.read_csv('data/negative-words.txt',skiprows=34, header='infer')['words'])
        
        except:
            print('Error reading Lexicons. Please check if lexicon files are in data directory...')
        
        
        try:
        
            # concat messages for easy processing
            all_messages = df_col.str.cat(sep=', ')
            
        except:
            print('Concat failed, please provide valid column of textual data')
        
        
        try:
        
            # sensing tokens
            word_tokens = re.findall(r'\b\w[\w-]*\b', all_messages.lower())
            
        except:
            print('Tokenization failed, please provide a valid column of textual data')
        
        # counting positive words
        positive_word_count = 0
        for word in word_tokens:
            if word in positive_words:
                positive_word_count += 1
        
        # counting negative words
        negative_word_count = 0
        for word in word_tokens:
            if word in negative_words:
                negative_word_count += 1
                
        return pd.DataFrame({'positive_words':positive_word_count, 'negative_words':negative_word_count}, index = [0])
    

def read_csv(csv_path = '', *args, **kwargs):
    """
    Read a comma-separated values (csv) file into NLPFrame.

    --------------
    Arguments:
        csv_path: str or path object
        *args: arguments to pass pd.read_csv function
        **kwargs: keyword arguments to pass pd.read_csv function

    --------------
    Return
        NLPFrame

    -------------
    Example
        >>> nlp.read_csv('./data/file.csv')
    """
    if csv_path == '':
        raise ValueError('Please provide path to the csv file')
    return NLPFrame(pd.read_csv(csv_path, *args, **kwargs))

def read_excel(path = '', *args, **kwargs):
    """
    Read an Excel file into a NLPFrame.

    --------------
    Arguments:
        path: str or path object
        *args: arguments to pass pd.read_excel function
        **kwargs: keyword arguments to pass pd.read_excel function

    --------------
    Return
        NLPFrame

    -------------
    Example
        >>> nlp.read_excel('./data/file.xlsx')
    """
    if path == '':
        raise ValueError('Please provide path to the excel file')
    return NLPFrame(pd.read_csv(read_excel, *args, **kwargs))

if __name__ == '__main__':
    # ex = pd.DataFrame({'text_col' : ['Today is a beautiful Monday and I would love getting a coffee. However, startbucks is closed.','It has been an amazing day today!']})
    # print(get_part_of_speech(ex['text_col']))
        
    ex2 = NLPFrame({'text_col': ['彼は新しい仕事に本当に満足している','It has been an amazing day today!']})
    print(ex2.get_nlp_summary())

