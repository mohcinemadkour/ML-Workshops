import xml.etree.cElementTree as etree
import re
from tqdm import tqdm
import os
import nltk
from bs4 import BeautifulSoup
from html2text import html2text 
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize,sent_tokenize
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
np.random.seed(7)

def clean_html(html):
    """
    Copied from NLTK package.
    Remove HTML markup from the given string.

    :param html: the HTML string to be cleaned
    :type html: str
    :rtype: str
    """

    # First we remove inline JavaScript/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    # Then we remove html comments. This has to be done before removing regular
    # tags since comments can contain '>' characters.
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    # Next we can remove the remaining tags:
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # Finally, we deal with whitespace
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()

def loadFiles(directory):
    DEBUG =False
    l = []
    for file in os.listdir(directory):
        data = directory + file
        if DEBUG : print (data)
        l.append(data)
    l=sorted(l)
    
    return l


def cleanDatset(holdtext):
    dataset=[]
    for i in tqdm(holdtext):        
        sent_tokenize_list = sent_tokenize(i)
        tokenized_reports = [word_tokenize(report) for report in sent_tokenize_list]
        regex = re.compile('[%s]' % re.escape(string.punctuation)) #see documentation here: http://docs.python.org/2/library/string.html
        tokenized_reports_no_punctuation = []
        
        for review in tokenized_reports:
            new_review = []
            for token in review: 
                new_token = regex.sub(u'', token)
                if not new_token == u'':
                    new_review.append(new_token)
            tokenized_reports_no_punctuation.append(new_review)    
        tokenized_reports_no_stopwords = []
        for report in tokenized_reports_no_punctuation:
            new_term_vector = []
            for word in report:
                if not word in stopwords.words('english'):
                    new_term_vector.append(word)
            tokenized_reports_no_stopwords.append(new_term_vector)
        v=[]
        for i in tokenized_reports_no_stopwords:
            v.append(" ".join(i))
        gt=" ".join(v)
        text2=''.join([i for i in gt if not i.isdigit()])
        toker = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
        fnlTxt=''.join(toker.tokenize(text2))
        dataset.append(" ".join(fnlTxt.split()))
    return dataset

