#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    loaded_iris = load_iris()
    exp_tot = loaded_iris.data
    resp_tot = loaded_iris.target
    train_X, test_X, train_y, test_y = train_test_split(exp_tot, resp_tot, train_size=0.80, random_state=0)
    gaus_model = naive_bayes.GaussianNB()
    gaus_model.fit(train_X, train_y)
    pred_y = gaus_model.predict(test_X)
    acc_score = metrics.accuracy_score(test_y, pred_y)
    return acc_score

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
