#!/usr/bin/env python3
import gzip
import pandas as pd
import numpy as np
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def spam_detection(random_state=0, fraction=1):
    ham_list = []
    with gzip.open('src/ham.txt.gz', 'rb') as f:
        for line in f:
            ham_list.append(line.decode().strip())
    spam_list = []
    with gzip.open('src/spam.txt.gz', 'rb') as g:
        for line in g:
            spam_list.append(line.decode().strip())
    lg_h_list, lg_s_list = (math.floor(len(ham_list) * fraction), math.floor(len(spam_list) * fraction))
    resp_vars = np.array([0 for i in range(lg_h_list)] + [1 for j in range(lg_s_list)])
    model = CountVectorizer()
    feat_matrix = model.fit_transform(np.array(ham_list[0:lg_h_list] + spam_list[0:lg_s_list]))
    X_train, X_test, y_train, y_test = train_test_split(feat_matrix, resp_vars, train_size=.75, test_size=.25, random_state=random_state)
    mnb_model = MultinomialNB()
    mnb_model.fit(X_train, y_train)
    pred = mnb_model.predict(X_test)
    acc_score = accuracy_score(y_test, pred)
    return acc_score, X_test.shape[0], math.floor((X_test.shape[0] * (1-acc_score)))



def main():
    accuracy, total, misclassified = spam_detection(fraction=0.1)
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
