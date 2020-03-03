from nlpsummarize import nlpsummarize
import pandas as pd


def check_pos_func():
    def english_input_1():
        true_results = pd.DataFrame({'adjective': 0.0741, 'noun': 0.2222, 'verb': 0.2963})
        initial_df = pd.DataFrame({'text_col' : ['Today is a beautiful Monday and I would love getting a coffee. However, startbucks is closed.','It has been an amazing day today!']})
        
        res = nlpsummarize.part_of_speech.get_part_of_speech(initial_df['text_col'])
        assert res.columns == ['adjective', 'noun', 'verb'], 'Defualt columns should be adjective, noun and verb'
        assert res == true_results, 'The result is not correct for basic input'

    def chinese_input_1():
        initial_df = pd.DataFrame({'text_col': ['彼は新しい仕事に本当に満足している']})
        res = get_part_of_speech(initial_df['text_col'])

        assert res, 'The function should return an output even for non-English text'
        

    def mixture_input_1():
        initial_df = pd.DataFrame({'text_col': ['彼は新しい仕事に本当に満足している','It has been an amazing day today!']})
        res = get_part_of_speech(ex2['text_col'])

        assert res, 'The function should return an output even for mixture of English and non-English sentences!'

    english_input_1()
    chinese_input_1()
    mixture_input_1()
