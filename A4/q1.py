import math as m
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

CLUSTER = 0
COLORS = ['r', 'g', 'b', 'y', 'm']


def get_points(filename):
    points = []
    with open(filename) as file:
        for line in file:
            point = [float(x) for x in line.split()]
            points.append(point)
    return points


def smallest_singlelink_dist(points):
    min = None
    for i in range(len(points)):
        for j in range(i, len(points)):
            p1 = points[i]
            p2 = points[j]
            if p1[CLUSTER] == p2[CLUSTER]:
                continue
            if min == None:
                min = [p1, p2]
                continue
            if i == 2 and j == 3:
                pass
            if j == 2 and i == 3:
                pass

            old = m.dist(min[0][1:], min[1][1:])
            new = m.dist(p1[1:], p2[1:])
            # compare current distance to minimum distance
            if new < old:
                min = [p1, p2]
    min_dist = m.dist(min[0], min[1])
    return min


def smallest_completelink_dist(clusters):
    """
    goal: find the largest distance between each pair of clusters
    from that find the smallest "max" distance
    """
    min = [clusters[0], clusters[1]]
    min_dist = 9999999
    for i in range(len(clusters)):
        for j in range(i, len(clusters)):
            if clusters[i] == clusters[j]: continue
            temp = [clusters[i], clusters[j]]
            temp_dist = distance_between_clusters(clusters[i], clusters[j])
            if temp_dist < min_dist:
                min = temp
                min_dist = temp_dist

    return min

            
def distance_between_clusters(cluster1, cluster2):
    max = 0
    for point1 in cluster1:
        for point2 in cluster2:
            p1 = point1[1:]
            p2 = point2[1:]
            dist = m.dist(p1, p2)
            if dist > max:
                max = dist
    return max
            


def plot_points(points):
    fig, ax = plt.subplots()
    for i in range(len(points)):
        color = ""
        if points[i][CLUSTER] == 2:
            color = COLORS[0]
        elif points[i][CLUSTER] == 4:
            color = COLORS[1]
        else:
            color = COLORS[2]
        ax.plot(points[i][1], points[i][2], marker='o', color=color)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_title('Plot')

    plt.show()



def print_points(points):
    for point in points:
        print("(", point[1], ", ", point[2], ")")

        

# part a, single link
def a_single_link():
    k = 3
    points = get_points("C1.txt")
    clusters = points.copy()

    while len(clusters) > k:
        min = smallest_singlelink_dist(clusters)        
        p1 = min[0]
        p2 = min[1]
            
        for point in points:
            if point[CLUSTER] == p1[CLUSTER]:
                point[CLUSTER] = p2[CLUSTER]

        new_cluster = np.mean(min, axis=0).tolist()
        new_cluster[0] = p2[CLUSTER]
        clusters.remove(p1)
        clusters.remove(p2)
        clusters.append(new_cluster)
    
    for point in points:
        print(point)
    plot_points(points)
    

    
# part a, complete link
def a_complete_link():
    k = 3
    points = get_points("C1.txt")
    clusters = []
    for p in points:
        clusters.append([p])
    
    count = 0
    while len(clusters) > k:
        print(count)
        count += 1

        min = smallest_completelink_dist(clusters)        
        c1 = min[0]
        c2 = min[1]

        for cluster in c1:
            c2.append(cluster)

        clusters.remove(c1)

    fig, ax = plt.subplots()
    for i in range(len(clusters)):
        color = COLORS[i]
        for j in range(len(clusters[i])):
            ax.plot(clusters[i][j][1], clusters[i][j][2], marker="o", color=color)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_title('Plot')

    plt.show()
        

def Q_1_b():
    k = 3
    points = np.array(get_points("C1.txt"))
    clustering = AgglomerativeClustering(k, linkage="single").fit(points)
    print(clustering.labels_)




       
    



#a_single_link()
#a_complete_link()
Q_1_b()