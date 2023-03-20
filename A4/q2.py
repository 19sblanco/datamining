import math
import matplotlib.pyplot as plt
import numpy as np 
import random
from sklearn.cluster import KMeans

COLORS = ['r', 'g', 'b', 'y', 'm']


def pick_number_with_probability(lst):
    epsilon = 1e-10
    total = sum(lst)

    rand_num = random.uniform(epsilon, total)

    running_total = 0
    for i in range(len(lst)):
        num = lst[i]
        running_total += num
        if running_total >= rand_num:
            return i

    return -1

def k_center_clustering(X, k): # gonzolas
    phi = [0] * len(X)
    sites = []
    sites.append(X[0])
    centers = [0]

    for i in range(1, k):
        m = 0
        s_i = 0
        for j in range(len(X)):
            x_j = X[j]
            if x_j in sites: continue
            site = X[phi[j]]
            distance = math.dist(x_j, site) 
            if distance > m:
                m = distance 
                s_i = j
        for j in range(len(X)):
            old = math.dist(X[j], X[phi[j]])
            new = math.dist(X[j], X[s_i])
            if old > new:
                phi[j] = s_i
        sites.append(s_i) 
        if s_i not in centers:
            centers.append(s_i)
    return phi, centers


def k_means_pp(X, k):
    phi = [0] * len(X)
    centers = [0]

    distances = [0] * len(X)
    for i in range(1, k):
        for j in range(len(X)):
            dist = math.dist(X[j], X[phi[j]])
            distances[j] = dist**2
        new_center = pick_number_with_probability(distances)
        for j in range(len(X)):
            old = math.dist(X[j], X[phi[j]])
            new = math.dist(X[j], X[new_center])
            if old > new:
                phi[j] = new_center
        centers.append(new_center)
    return phi, centers
    


def get_points(filename):
    points = []
    with open(filename) as file:
        for line in file:
            point = [float(x) for x in line.split()]
            points.append(point[1:])
    return points


def plot_points(k, points, centers, phi):
    fig, ax = plt.subplots()
    for i in range(k):
        center = centers[i]
        for j in range(len(points)):
            if phi[j] != center: continue
            ax.plot(points[j][0], points[j][1], marker="o", color=COLORS[i])

    for i in range(len(centers)):
        c = centers[i]
        ax.plot(points[c][0], points[c][1], marker="+", color=COLORS[i+1], markersize=15)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_title('Plot')

    plt.show()

            

def k_center_cost(X, centers):
    max = 0
    for i in range(len(X)):
        dist = math.dist(X[i], X[centers[i]])
        if dist > max:
            max = dist
    return max


def k_means_cost(X, centers, normalize=False):
    sum = 0
    for i in range(len(X)):
        dist = math.dist(X[i], X[centers[i]])
        sum += dist**2
    if normalize == False:
        return sum
    else:
        return math.sqrt(sum / len(X))
    
    

def two_b_i(points, k):
    phi, center_centers = k_center_clustering(points, k)
    cost = k_means_cost(points, phi)
    print(cost)

    trials = 20
    x_vals = []
    count = 0
    for i in range(trials):
        phi, k_means_centers = k_means_pp(points, k)
        cost = k_means_cost(points, phi)
        if k_means_centers == center_centers: count += 1
        x_vals.append(cost)

    print("they are the same", count)

    y_vals = []
    for i in range(trials):
        val = i / trials
        y_vals.append(val)


    x_vals.sort()
    plt.xlabel("4 means cost")
    plt.ylabel("poportion with that value")
    plt.title("cumulative density function")
    plt.plot(x_vals, y_vals)
    plt.show()


def two_c_iii(X, k):
    costs = []
    count = 0
    for i in range(20):
        phi, c = k_means_pp(X, k)
        init = np.array([X[c[0]], X[c[1]], X[c[2]], X[c[3]]])
        
        kmeans = KMeans(n_clusters=k, init=init)
        kmeans.fit(X)
        cost = kmeans.inertia_
        costs.append(cost)
        if init.tolist() == kmeans.cluster_centers_.tolist():
            count += 1

    print(count)

    y_vals = []
    for i in range(20):
        y_vals.append(i / 20)
    costs.sort()
    plt.xlabel("4 means cost")
    plt.ylabel("poportion with that value")
    plt.title("cumulative density function")
    plt.plot(costs, y_vals)
    plt.show()
    




def two_c_i(X, k, init_points):
    newX = X
    X = np.array(X)
    # define your own initial cluster centers
    initial_centers = np.array(
        init_points
    )

    # initialize the KMeans model with the desired number of clusters and initial centers
    kmeans = KMeans(n_clusters=k, init=initial_centers)

    # fit the model to the data
    kmeans.fit(X)

    # get the cluster centers and labels
    cluster_centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    # question
    cost = kmeans.inertia_
    print(cost)

    # plot the data points
    plt.scatter(X[:, 0], X[:, 1], c=labels)
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', color='r', s=100)
    plt.show()





        







def two():
    k = 4
    points = get_points("C2.txt")

    # 2_a
    # phi, centers = k_center_clustering(points, k)
    # plot_points(k, points, centers, phi)
    # cost = k_center_cost(points, phi)
    # print("4 center cost", cost)
    # cost = k_means_cost(points, phi, normalize=True)
    # print("4 means cost", cost)

    # 2_b
    # two_b_i(points, k)
    
    # 2_c
    # two_c_i(points, k, [points[0], points[1], points[2], points[3]])
    # phi, c = k_center_clustering(points, k)
    # two_c_i(points, k, [points[c[0]], points[c[1]], points[c[2]], points[c[3]]])
    two_c_iii(points, k)









"""
add up how far each point is from its cluster centroid
"""







two()