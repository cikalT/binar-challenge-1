import re
import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

alay_dict = pd.read_csv('data/new_kamusalay.csv', encoding='latin-1', header=None)
alay_dict = alay_dict.rename(columns={0: 'original', 1: 'replacement'})

id_stopword_dict = pd.read_csv('data/stopwordbahasa.csv', header=None)
id_stopword_dict = id_stopword_dict.rename(columns={0: 'stopword'})


def lowercase(text):
    return text.lower()


def remove_punctuation_mark(text):
    return re.sub(r'[^\w\s]', '', text)


def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols and pictographs
                               u"\U0001F680-\U0001F6FF"  # transport and map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags for IOS
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def preprocess_text(text):
    # text = lowercase(text) 
    text = remove_punctuation_mark(text)
    text = remove_emojis(text)
    return text


def preprocess_file(file):
    file['Tweet'] = file['Tweet'].apply(preprocess_text)
    return file
