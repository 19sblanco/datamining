import sklearn.datasets as dt
import random
random.seed(75)
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.random_projection import GaussianRandomProjection
from sklearn.random_projection import SparseRandomProjection
from sklearn.random_projection import johnson_lindenstrauss_min_dim
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np



sample_size = 500

def prepare_data_problem_2():
    '''
        Fetch and downsample RCV1 dataset to only 500 points.
        https://scikit-learn.org/stable/datasets/real_world.html#rcv1-dataset 
    '''
    rcv1 = dt.fetch_rcv1()

    # Choose 500 samples randomly
    sample_size = 500
    row_indices = random.sample(list(range(rcv1.data.shape[0])),sample_size)
    data_sample = rcv1.data[row_indices,:]

    print(f'Shape of the input data: {data_sample.shape}') # Should be (500, 47236)
    return data_sample



"""
plan:
    onces for guassian random projection and sparse random projection
    https://scikit-learn.org/stable/modules/random_projection.html
    1. calculate pair wise distances of real points (do once)
    2. find appropriate values of (error) epsilon
    3. for each appropriate epison value:
        calculate the pair waise differences of new graph
        calculate the difference of the new graph and the original graph
        calculate the mean of the absolute differences
"""
def guassian(data):
    old_distances = euclidean_distances(data, data)

    eps = [0.1, 0.3, 0.5, 0.7, 0.9]
    min_n_components = johnson_lindenstrauss_min_dim(sample_size, eps=eps)

    plot_eps = []
    mean_vals = []
    bools = []
    for i in range(len(min_n_components)):
        if min_n_components[i] >= sample_size: continue

        plot_eps.append(eps[i])

        transformer = GaussianRandomProjection(eps=eps[i])
        data_new = transformer.fit_transform(data)

        new_distances = euclidean_distances(data_new, data_new)

        diff_matrix = abs(old_distances - new_distances)
        mean_val = np.mean(diff_matrix)

        mean_vals.append(mean_val)

        bool = test_johnson_lindenstruass(old_distances, new_distances, eps[i])
        bools.append(bool)

    
    # i
    plt.plot(plot_eps, mean_vals)
    plt.xlabel("epsilon")
    plt.ylabel("mean absolute differences")
    plt.show()

    # ii
    plt.hist(diff_matrix)
    plt.xlabel("value")
    plt.ylabel("frequency")
    plt.show()

    # iii 
    print(bools)

    
def test_johnson_lindenstruass(old_data_pair_dist, new_data_pair_dist, eps):
    norm_old = np.linalg.norm(old_data_pair_dist)
    norm_new = np.linalg.norm(new_data_pair_dist)

    lower_bounds = (1 - eps) * norm_old**2
    upper_bounds = (1 + eps) * norm_old**2
    middle = norm_new**2

    return lower_bounds <= middle <= upper_bounds

def sparse(data):
    old_distances = euclidean_distances(data, data)

    eps = [0.1, 0.3, 0.5, 0.7, 0.9]
    min_n_components = johnson_lindenstrauss_min_dim(sample_size, eps=eps)
    print("min n: ", min_n_components)

    plot_eps = []
    mean_vals = []
    bools = []
    for i in range(len(min_n_components)):
        if min_n_components[i] >= sample_size: continue

        plot_eps.append(eps[i])

        transformer = SparseRandomProjection(eps=eps[i])
        data_new = transformer.fit_transform(data)

        new_distances = euclidean_distances(data_new, data_new)

        diff_matrix = abs(old_distances - new_distances)
        mean_val = np.mean(diff_matrix)

        mean_vals.append(mean_val)

        
        bool = test_johnson_lindenstruass(old_distances, new_distances, eps[i])
        bools.append(bool)

    
    # i
    plt.plot(plot_eps, mean_vals)
    plt.xlabel("epsilon")
    plt.ylabel("mean absolute differences")
    plt.show()

    # ii
    # plt.hist(diff_vector)
    plt.hist(diff_matrix)
    plt.xlabel("value")
    plt.ylabel("frequency")
    plt.show()

    # iii 
    print(bools)



def test(data):
    # transformer = SparseRandomProjection(eps=.1)
    # print(data)
    # exit()
    transformer = SparseRandomProjection()
    data_new = transformer.fit_transform(data)
    print(data_new)


def main():
    data_sample = prepare_data_problem_2()
    guassian(data_sample)
    # sparse(data_sample)

    # test(data_sample)
    


"""
plan:
    onces for guassian random projection and sparse random projection
    https://scikit-learn.org/stable/modules/random_projection.html
    1. calculate pair wise distances of real points (do once)
    2. find appropriate values of (error) epsilon
    3. for each appropriate epison value:
        calculate the pair waise differences of new graph
        calculate the difference of the new graph and the original graph
        calculate the mean of the absolute differences
"""


main()