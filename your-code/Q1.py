import re
import os
def get_bow_from_docs(docs, stop_words=[]):
    corpus = []
    corpus = [f for f in os.listdir(docs) if f.endswith('.txt')]#aquí me da los paths de los documentos
    corpus_content = []
    for f in corpus:
        st = open(os.path.join(docs, f))
        corpus_content.append(st.read())
    #Convierte corpus_content sin puntos y minisculas.
    regex = re.compile('[^a-zA-Z]')
    corpus_content_filtered = [regex.sub(' ', i) for i in corpus_content]
    new_corpus = [p.lower() for p in corpus_content_filtered]
    #Nos devolverá bag_of_words
    bag_of_words = []
    a = ([i.split() for i in new_corpus])
    for x in a:
        for y in x:
            if y in bag_of_words:
                continue
            else:
                bag_of_words.append(y)
    #Nos devolverá ahora la frecuencia
    term_freq = []
    variable = []
    for i in new_corpus:
        variable = []  # se asigna una variable para guardarlos en una lista de listas
        for y in bag_of_words:
            variable.append(i.split().count(y))
        term_freq.append(variable)
    return {
        "bag_of_words": bag_of_words,
        "term_freq": term_freq
    }
print(get_bow_from_docs('C:/Users/952820/lab-string-operations/your-code'))

import re
from sklearn.feature_extraction import stop_words
import os
def remove_html_tags(corpus_content):
    clean = re.compile('<.*?>')
    corpus_content_html = re.sub(clean, '', corpus_content)
    return corpus_content_html
def remove_punctuation_lower(corpus_content):
    regex = re.compile('[^a-zA-Z]')
    corpus_content_filtered = regex.sub(' ', corpus_content).lower()
    return corpus_content_filtered
def remove_unicode(new_corpus):
    new_corpus2 = (new_corpus.encode('ascii', 'ignore')).decode("utf-8")
    return new_corpus2
def get_bow_from_docs(docs, stop_words=[]):
    # In the function, first define the variables you will use such as `corpus`, `bag_of_words`, and `term_freq`.
    corpus = []
    bag_of_words = []
    term_freq = []
    corpus_content = [remove_html_tags(i) for i in docs]
    corpus_content = [remove_punctuation_lower(i) for i in docs]
    corpus_content = [remove_unicode(i) for i in docs]
    # write your codes here
    a = ([i.split() for i in corpus_content])
    for x in a:
        for y in x:
            if y in bag_of_words:
                continue
            else:
                if y in stop_words:
                    continue
                else:
                    bag_of_words.append(y)
        for i in corpus_content:
            variable = []  # se asigna una variable para guardarlos en una lista de listas
            for y in bag_of_words:
                variable.append(i.split().count(y))
            term_freq.append(variable)
    return {
        "bag_of_words": bag_of_words,
        "term_freq": term_freq
    }

bow = get_bow_from_docs([
    'www.coursereport.com_ironhack.html',
    'en.wikipedia.org_Data_analysis.html',
    'www.lipsum.com.html'
],
    stop_words.ENGLISH_STOP_WORDS
)

print(bow)


