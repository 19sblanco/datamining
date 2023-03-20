import random as r
import numpy as np
import matplotlib.pyplot as plt
import time as t


n_list = [100,600,1100]
m_list = [500,1000,2000]

def question_2a(n):
    numbers_seen = []
    num_trials = 0

    while True:
        trial = r.randint(0, n)
        num_trials += 1

        if trial not in numbers_seen:
            numbers_seen.append(trial)
        else:
            pass

        if len(numbers_seen) == n:
            break
    
    return num_trials

def test(n, m):
    the_ks = []

    for i in range(m):
        k = question_2a(n)
        the_ks.append(k)

    sum_ks = sum(the_ks)
    average = sum_ks / m
    print(average)



def main(m):
    times = []
    for n in n_list:
        start = t.time()
        test(n, m)
        end = t.time()
        times.append(end - start)

    plt.xlabel("values of n")
    plt.ylabel("time for each n")
    plt.title("m = " + str(m))
    plt.plot(n_list, times)
    plt.show()


main(m_list[2])



# def question_2b():
#     n = 1000
#     m = 500
#     the_ks = []

#     for i in range(m):
#         k = question_2a(n)
#         the_ks.append(k)

#     the_ks.sort()

#     y = []
#     for i in range(m):
#         num_success = 0
#         k = the_ks[i]
#         for val in the_ks:
#             if val <= k:
#                 num_success += 1
#         fraction = num_success / m
#         y.append(fraction)


#     sum = 0
#     for val in the_ks:
#         sum += val
#     print(sum / m)