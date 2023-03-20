import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer 

def n_grams_sklearn():
    # Let's read some data 
    url = "https://raw.githubusercontent.com/koaning/icepickle/main/datasets/imdb_subset.csv"
    df = pd.read_csv(url) # This is how you read a csv file to a pandas frame
    corpus = list(df['text']) 
    corpus_small = corpus[:4] # This is a list of 4 movie reviews

    '''
    Read documentation for https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
    Complete 1.A by using CountVectorizer, its methods, and adjusting certain parameters.
    '''

    # Your code should go here: 
    # i

    

    # print("char, 2grams")
    # vectorizer = CountVectorizer(analyzer="char", ngram_range=(2,2))
    # x = vectorizer.fit_transform(corpus_small)
    # x_greaterthan0 = []
    # for i in range(4):
    #     for item in x.toarray()[i]:
    #         if int(item) > 0:
    #             x_greaterthan0.append(item)
    #     print(len(x_greaterthan0))
    #     x_greaterthan0 = []



    # print("char, 3grams")
    # vectorizer = CountVectorizer(analyzer="char", ngram_range=(3,3))
    # x = vectorizer.fit_transform(corpus_small)
    # x_greaterthan0 = []
    # for i in range(4):
    #     for item in x.toarray()[i]:
    #         if int(item) > 0:
    #             x_greaterthan0.append(item)
    #     print(len(x_greaterthan0))
    #     x_greaterthan0 = []

    # print("word, 2grams")
    # vectorizer = CountVectorizer(analyzer="word", ngram_range=(2,2))
    # x = vectorizer.fit_transform(corpus_small)
    # x_greaterthan0 = []
    # for i in range(4):
    #     for item in x.toarray()[i]:
    #         if int(item) > 0:
    #             x_greaterthan0.append(item)
    #     print(len(x_greaterthan0))
    #     x_greaterthan0 = []

    # print("testing generalization")
    # d_1 = ["I am", "am Sam"]
    # d_2 = ["Sam I", "I am"]
    # d_3 = [["I do"], ["do not"], ["not like"], ["like green"], ["green eggs"], ["eggs and"], ["and ham"]]
    # d_4 = [["I do"], ["do not"], ["not like"], ["like them"], ["them Sam"], ["Sam I"], ["I am"]]
    # throw_away = 0
    # Js = generalized_set_simularities(d_1, d_2, 1, 0, 0, 1, throw_away)
    # print(Js)
    # exit()

    # vectorizer = CountVectorizer(analyzer="word", ngram_range=(2,2))
    # X = vectorizer.fit_transform([corpus_small[0]])
    # # X = vectorizer.fit_transform(corpus_small)

    # print(vectorizer.get_feature_names())
    # exit()

    n_grams_types = [["char", (2,2)], ["char", (3,3)], ["word", (2,2)]]

    for n_gram_type in n_grams_types:
        print("n_gram_type", n_gram_type)
        analyzer = n_gram_type[0]
        ngram_range = n_gram_type[1]

        vectorizer = CountVectorizer(analyzer=analyzer, ngram_range=ngram_range)
        x = vectorizer.fit_transform(corpus_small)


        for i in range(len(corpus_small)-1):
            for j in range(i + 1, len(corpus_small)):
                x = vectorizer.fit_transform([corpus_small[i]])
                d_1 = vectorizer.get_feature_names()
                y = vectorizer.fit_transform([corpus_small[j]])
                d_2 = vectorizer.get_feature_names()
                
                Js = generalized_set_simularities(d_1, d_2, 1, 0, 0, 1, None)

                print("doc: ", str(i), str(j), str(Js))
                
    



def union(ls1, ls2):
    new_list = []
    for item in ls1:
        new_list.append(item)

    for item in ls2:
        if item not in ls1:
            new_list.append(item)
    return new_list

def intersection(ls1, ls2):
    new_list = []
    for item in ls1:
        if item in ls2:
            new_list.append(item)
    return new_list

def set_minus(ls1, ls2):
    new_list = []
    for item in ls1:
        if item not in ls2:
            new_list.append(item)
    return new_list

def generalized_set_simularities(A, B, x, y, z, z_prime, n):
    x_part = 0
    y_part = 0
    z_part = 0
    z_prime_part = 0
    if x != 0:
        x_part = len(intersection(A, B))
    if y != 0:
        y_part = len(set_minus(n, union(A, B)))
    if z != 0:
        z_part = len(set_minus(union(A, B), intersection(A, B)))
    if z_prime != 0:
        z_prime_part = len(set_minus(union(A, B), intersection(A, B)))
    
    top = x_part + y_part + z_part
    bottom = x_part + y_part + z_prime_part

    return top / bottom

def jaccard(x, y):
    top = len(intersection(x, y))
    bottom = len(intersection(x, y)) + len(set_minus(union(x, y), intersection(x, y)))
    return top / bottom



n_grams_sklearn()




"""
n is the set of all possible grams for a problem
its the len of get_names_out
"""