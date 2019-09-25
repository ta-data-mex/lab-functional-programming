import re
from sklearn.feature_extraction import stop_words


def strip_html_tags(texto):
    return re.compile('<.*?>').sub('', texto)


def remove_punctuation(texto):
    return texto.compile('^\w\s').sub('', texto)


def to_lower_case(texto):
    return texto.lower()


def get_bow_from_docs(docs, stop_words=[]):
    # In the function, first define the variables you will use such as `corpus`, `bag_of_words`, and `term_freq`.
    corpus = []
    for doc in docs:
        corpus.append(open(doc, 'r', encoding='utf8').read())
        corpus2 = []

    for i in corpus:
        corpus2.append(to_lower_case(remove_punctuation))
    bag_of_words = []

    for i in corpus2:
        words = i.split()
        for w in words:
            if w not in bag_of_words and w not in stop_words:
                bag_of_words.append(w)

    # notin_stopwords = [item for item in bag_of_words if item not in stop_words]
    print(bag_of_words)
    term_freq = []
    items = []

    for i in corpus2:
        items.append(i.split())

    for i in range(len(items)):
        temp = []
        for y in bag_of_words:
            temp.append(items[i].count(y))
        term_freq.append(temp)

    # Now return your output as an object
    return {
        "bag_of_words": bag_of_words,
        "term_freq": term_freq
    }

bow = get_bow_from_docs([
        'www.coursereport.com_ironhack.html',
        'en.wikipedia.org_Data_analysis.html',
        'www.lipsum.com.html'
    ], stop_words.ENGLISH_STOP_WORDS)


