from sklearn.feature_extraction import stop_words
# Define function
def get_bow_from_docs(docs, stop_words=[]):
    # In the function, first define the variables you will use such as `corpus`, `bag_of_words`, and `term_freq`.
    corpus = []
    for doc in docs:
        corpus.append(open(doc, 'r').read())
        corpus2 = []
    """
    Loop `docs` and read the content of each doc into a string in `corpus`.
    Remember to convert the doc content to lowercases and remove punctuation.
    """

    for i in corpus:
        corpus2.append(i.lower().replace(".", ""))
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

    """
    Loop `corpus`. Append the terms in each doc into the `bag_of_words` array. The terms in `bag_of_words` 
    should be unique which means before adding each term you need to check if it's already added to the array.
    In addition, check if each term is in the `stop_words` array. Only append the term to `bag_of_words`
    if it is not a stop word.
    """

    """
    Loop `corpus` again. For each doc string, count the number of occurrences of each term in `bag_of_words`. 
    Create an array for each doc's term frequency and append it to `term_freq`.
    """

    # Now return your output as an object
    return {
        "bag_of_words": bag_of_words,
        "term_freq": term_freq
    }

# Define doc paths array


docs = ['doc1.txt','doc2.txt','doc3.txt']

# Obtain BoW from your function
bow = get_bow_from_docs(docs)

# Print BoW
print(bow)