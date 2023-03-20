import numpy as np
import time


def misra_gries(A, k):
    C = [0] * (k-1)
    L = [None] * (k-1)

    for i in range(len(A)):
        next = False
        for j in range(len(L)):
            if A[i] == L[j]:
                C[j] += 1
                next = True
                break
        if next: continue

        for j in range(len(C)):
            if C[j] == 0:
                L[j] = A[i]
                C[j] = 1
                next = True
                break
        if next: continue
        for j in range(len(C)):
            C[j] -= 1
    return C, L

def q_1_a():
    stream = open("S1.txt", "r").read()
    k = 12
    C, L = misra_gries(stream, k)
    print("\tc", C)
    print("\tl", L)
    print("===")
    m = len(stream)
    ratio = [round(x/m, 3) for x in C]
    print("ratio actual: ", ratio)
    ratio_c = [round((x+(m/k))/m, 3) for x in C]
    print("ratios might: ", ratio_c)
    ratio_c_next = [round((x-(m/k))/m, 3) for x in C]
    print("ratios must: ", ratio_c_next)


def count_min_sketch(A, k, t):
    np.random.seed(1)

    # get the 6 random hash functinos
    hash_funcs = []
    for i in range(t):
        b = np.random.randint(0, k)
        hash_funcs.append(lambda x: (ord(x) + b) % k)

    C = np.full((k, t), 0)
    for i in range(len(A)):
        for j in range(t):
            row = hash_funcs[j](A[i])
            C[row][j] += 1
            
    return C, hash_funcs




def q_2_a():
    stream = open("S1.txt", "r").read()
    k = 12
    t = 6
    C, hash_funcs = count_min_sketch(stream, k, t)

    chars = ["a", "b", "c"]
    for char in chars:
        min = 999999999
        for i in range(t):
            hash_val = hash_funcs[i](char)
            count = C[hash_val][i]
            if count < min:
                min = count
        # print(char, " count is :", min)
        # print(char, "ratio: ", round(min / len(stream), 3))
        min_w = (min - ((2 * len(stream)) / k)) / len(stream)
        print(char, "ratio - W ", round(min_w, 3))

        





def main():
    # q_1_a()
    q_2_a()



def test():
    start = time.time()
    stream = open("S1.txt", "r").read()
    k = 12
    t = 6
    C, hash_funcs = count_min_sketch(stream, k, t)
    print(time.time() - start)

    start = time.time()
    stream = open("S1.txt", "r").read()
    k = 12
    C, L = misra_gries(stream, k)
    print(time.time() - start)
   


test()
# main()
