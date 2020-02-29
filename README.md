## nlpsummarize 

Python package that provides a nice summary of all character columns in a pandas dataframe.

### Overview:

One of the most relevant applications of machine learning for corporations globally is the use of natural language processing (NLP). Whether it be parsing through business documents to gather key word segments or detecting Twitter sentiment of a certain product, NLP’s use case is prevalent in virtually every business environment.

Unfortunately, there are few tools today which provide summary statistics on textual data that a user may want to analyze. Our goal with this package is to provide users with a simple and flexible tool to gather key insights that would be useful during the exploratory data analysis phase of the data science workflow. 

Our library specifically will make extensive use of pre-existing packages in the Python eco-system. We will use the [`nltk`](https://www.nltk.org/)  library to build most of the sentiment analysis functions while also leveraging well-known packages such as [`pandas`](https://pandas.pydata.org/) to aid in the overall presentation of our final output results. 


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
- textblob==0.15.3

### Usage

This is a basic example which shows you how to generate a summary:

``` python

import nlpsummarizer
df = pd.DataFrame({'text_col' : ['I love travelling to Japan and
                                eating Mexican food but I can only speak
                                English!']})
detect_language(df['text_col'])
[1]  'English'

get_part_of_speech(df['text_col'])
[2]  |   verbs    | prepositions | adjectives |   nouns   |  articles  |
     |    0.2     |     0.11     |     0.3    |    0.06   |     0.18   |

get_polarity(df['text_col'])
[3] | positive words | negative words | neutral words |
    |         3      |           0    |    15         |

summary_4(df['text_col'])
[4] | number of sentences | number of stop words | high freq. words |
    |         1           |           4          |    I(2)          |
```

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
