#!/usr/bin/env python3

import scipy
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    iris = load_iris()
    k_model = KMeans(n_clusters=3, random_state=2)
    v_model = KMeans(n_clusters=3, random_state=0)
    k_model.fit(iris.data)
    perm = find_permutation(3, iris.target, k_model.labels_)
    new_labels = [perm[label] for label in k_model.labels_]
    acc = accuracy_score(iris.target, new_labels)
    return acc

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
