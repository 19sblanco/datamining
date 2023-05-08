import sklearn.datasets as dt
import random
random.seed(75)
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np


def prepare_data_problem_1():    
    # Downloads from https://www.gapminder.org/data/
    cm_path = 'child_mortality_0_5_year_olds_dying_per_1000_born.csv'
    fe_path = 'children_per_woman_total_fertility.csv'
    cm = pd.read_csv(cm_path).set_index('country')['2017'].to_frame()/10
    fe = pd.read_csv(fe_path).set_index('country')['2017'].to_frame()
    child_data = cm.merge(fe, left_index=True, right_index=True).dropna()
    child_data.columns = ['mortality', 'fertility']
    child_data.head()
    # print (child_data)

    return child_data


def joint_scatter_plot(data, approx_data=None): 
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(data['mortality'],data['fertility'], color='b')
    if approx_data != None: 
        ax1.scatter(approx_data['mortality'],approx_data['fertility'], color='r')
    plt.show()


def center_data(data):
    mor = []
    for m in data['mortality']:
        mor.append(m)
    avg_mor = sum(mor) / len(mor)
    mortality = [x - avg_mor for x in mor]

    fer = []
    for f in data['fertility']:
        fer.append(f)
    avg_fer = sum(fer) / len(fer)
    fertility = [x - avg_fer for x in fer]

    result = [[x, y] for x, y in zip(mortality, fertility)]
    return result, avg_mor, avg_fer



def p1i(data):
    centered_data, avg_mor, avg_fer = center_data(data)
    centered_data = np.array(centered_data)
    u, s, vh = np.linalg.svd(centered_data)

    origin = np.array([[0, 0],[0, 0]])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.scatter(centered_data[:,0], centered_data[:,1], color='b')
    ax2.quiver(*origin, vh[:,0], vh[:,1], color=['r','b'])
    plt.show()


def p1ii(data):
    centered_data, avg_mor, avg_fer = center_data(data)
    centered_data = np.array(centered_data)
    u, s, vh = np.linalg.svd(centered_data, full_matrices=False)

    s[1] = 0
    approx_data = u.dot(np.diag(s).dot(vh))

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(centered_data[:,0], centered_data[:,1], color='b')
    ax1.scatter(approx_data[:,0],approx_data[:,1], color='r')
    plt.show()



def main():
    p1_data = prepare_data_problem_1()
    # p1i(p1_data)
    p1ii(p1_data)
    


main()

