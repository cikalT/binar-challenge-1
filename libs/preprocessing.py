import re


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
    text = remove_punctuation_mark(text)
    text = remove_emojis(text)
    return text


def preprocess_file(file):
    file['Tweet'] = file['Tweet'].apply(preprocess_text)
    return file
