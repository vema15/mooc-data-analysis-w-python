#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances
import scipy

from matplotlib import pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation


def toint(x):
    conversion = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }
    return conversion[x]

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep='\t')
    bind_info = [list(i) for i in list(df['X'])]
    label = list(df['y'])  
    conv_bind = []
    for i in bind_info:
        row = []
        for j in i:
            row.append(toint(j))
        conv_bind.append(row)
    return np.array(conv_bind), np.array(label)
    

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    features, labels = get_features_and_labels(filename)
    agg_model = AgglomerativeClustering(metric='euclidean', linkage="average")
    agg_model.fit(features)
    pred = agg_model.fit_predict(features)
    perm = find_permutation(2, labels, pred)
    new_labels = [perm[label] for label in pred]
    acc = accuracy_score(labels, new_labels)
    return acc

def cluster_hamming(filename):
    features, labels = get_features_and_labels(filename)
    agg_mod = AgglomerativeClustering(linkage='average', metric='precomputed')
    plabels = agg_mod.fit_predict(pairwise_distances(features, metric='hamming'))
    nlabels = find_permutation(2, labels, plabels)
    return accuracy_score(labels, [nlabels[x] for x in agg_mod.labels_])



def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
