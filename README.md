## nlpsummarize

Python package that provides a nice summary of all character columns in a pandas dataframe.

### Overview:

One of the most relevant applications of machine learning for corporations globally is the use of natural language processing (NLP). Whether it be parsing through business documents to gather key word segments or detecting Twitter sentiment of a certain product, NLP’s use case is prevalent in virtually every business environment.

Unfortunately, there are few tools today which provide summary statistics on textual data that a user may want to analyze. Our goal with this package is to provide users with a simple and flexible tool to gather key insights that would be useful during the exploratory data analysis phase of the data science workflow.

Our library specifically will make extensive use of pre-existing packages in the Python eco-system. We will use the [`nltk`](https://www.nltk.org/)  library to build most of the sentiment analysis functions while also leveraging well-known packages such as [`pandas`](https://pandas.pydata.org/) to aid in the overall presentation of our final output results.

To the best of our knowledge, there is no any other package that combines all the below mentioned functionality in one.

### Installation:

```
pip install -i https://test.pypi.org/simple/ nlpsummarize
```

### Features

Below are several functions in our Python package:

`detect_language`: This function will parse through the textual data and come up with the language of the text. This can be useful for an international company’s customer service process in detecting which regions are requesting the most help.

`part_of_speech`: This function will generate key statistics on the proportions of textual data points including verbs, prepositions, adjectives, nouns and articles.

`polarity`: This function will check the overall sentiment of the data by assessing the number of negative, positive and neutral words in the textual data.

`sentence_stopwords_freq`: This function will check the proportion on the number of sentences, stop words and also output high frequency words in the textual data.

### Dependencies

- pandas==1.0.1
- nltk==3.4.5
- fasttext==0.9.1
- itertools==8.0.2

Please note that the `fasttext` library must use the specific pre-trained model called `lid.176.bin` which can be downloaded [here](https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin).

### Usage

This is a basic example which shows you how to generate a summary:

``` python

from nlpsummarizer import nlp
df = nlp.NLPFrame({'text_col' : ['I love travelling to Japan and
                                eating Mexican food but I can only speak
                                English!']})
df.detect_language()
[1]   | language |
      |  English |

df.get_part_of_speech()
[2]  |  adjective  |  noun   |  verb   |
     |  0.125      |  0.125  |  0.3125 |

df.polarity()
[3] | positive words | negative words |
    |         1      |           0    |

df.summary_4()
[4] | number of sentences | number of stop words   |        high freq. words                |
    |         1           |           179          |    [(2, I), (1, travelling), (1, to)]  |
    
df.get_nlp_summary()
[5]   language | Number of sentences | Stop words  |                         Frequency   | adjective  | noun  |  verb  |  positive_words | negative_words |
  English      |              1      |       179   | [(2, I), (1, travelling), (1, to)]  |    0.125   | 0.125 | 0.3125 |            1    |             0  |

```

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
