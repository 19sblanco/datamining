import random as r
import time
import numpy as np
import matplotlib.pyplot as plt

n_list = [10_000, 100_000, 1_000_000]
m_list = [500, 1000, 10_000]

def question1a(n):
    trials = []

    while True:
        trial = r.randint(0, n)
        if trial in trials:
            trials.append(trial)
            break
        trials.append(trial)

    return len(trials)


def test(n, m):
    x = []
    for i in range(m):
        x.append(question1a(n))
    
    sum_x = sum(x)
    average = sum_x / m
    print(average)

def main(m):
    times = []
    for n in n_list:
        start = time.time()
        test(n, m)
        end = time.time()
        times.append(end - start)


    # fig = plt.figure()
    # ax = fig.add_axes([0,0,1,1])
    # ax.bar(n_list, times)
    # plt.show()

        
    plt.xlabel("values of n")
    plt.ylabel("time for each n")
    plt.title("m = " + str(m))
    plt.plot(n_list, times)
    plt.show()

 


main(m_list[2])


# def question2a():
#     x = [] # get k values
#     for i in range(500):
#         x.append(question1a(n_list[0]))
#     x.sort()

#     # y = [] # get number of trials sucessful with at most value of k (or x in this case)
#     # for i in range(1, 501):
#     #     num = 0
#     #     for val in x:
#     #         if val <= i:
#     #             num += 1      
#     #     y.append(num)

#     # for i in range(len(y)):
#     #     y[i] = y[i] / 500 # turn into a number <1


#     # plt.xlabel("number of trials")
#     # plt.ylabel("collision after k trials")

#     # plt.title("CDF for the number of collisions with randomness")
#     # plt.plot(x,y)
#     # plt.show()

#     ########## question 3

#     sum_x = 0
#     for i in range(len(x)):
#         sum_x += x[i]

#     print(sum_x / 500)