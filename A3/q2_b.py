import math as m
import random as r
import numpy as np
from numpy import log as ln
from numpy import linalg as LA
import matplotlib.pyplot as plt

t = 200
d = 100


def y_1(u1, u2):
    return m.sqrt(-2 * ln(u1)) * m.cos(2 * m.pi * u2)

def y_2(u1, u2):
    return m.sqrt(-2 * ln(u1)) * m.sin(2 * m.pi * u2)

def normalize(v):
    vector_norm = LA.norm(v, 2)
    for i in range(len(v)):
        v[i] = v[i] / vector_norm
    return v

def s_ang(a, b):
    dot = np.dot(a, b)
    if (dot > 1): dot = m.floor(dot)
    return 1 - (1/m.pi) * np.arccos(dot)


# generate 200 unit vectors using guassian random variables
unit_vectors = []
for i in range(200):
    vector = []
    for j in range(d // 2):
        u1 = r.uniform(0, 1)
        u2 = r.uniform(0, 1)
        y1 = y_1(u1, u2)
        y2 = y_2(u1, u2)
        vector.append(y1)
        vector.append(y2)
    unit_vector = normalize(vector)
    unit_vectors.append(unit_vector)

# dot_products = []
# for i in range(200):
#     for j in range(i + 1, 200):
#         product = np.dot(unit_vectors[i], unit_vectors[j])
#         dot_products.append(product)

# dot_products.sort()

# print(dot_products, "\n", len(dot_products))
# print(max(dot_products))
# print(min(dot_products))

# """
# x: dot product value
# y: index in array / len of array
# """
# y_values = []
# for i in range(len(dot_products)):
#     val = i / len(dot_products)
#     y_values.append(val)


# plt.xlabel("dot product values")
# plt.ylabel("porportion of dot products with that value")
# plt.title("guassian dot products")
# plt.plot(dot_products, y_values)
# plt.show()




angular_simularities = []
for i in range(200):
    for j in range(i + 1, 200):
        simularitiy = s_ang(unit_vectors[i], unit_vectors[j])
        angular_simularities.append(simularitiy)

angular_simularities.sort()

y_values = []
for i in range(len(angular_simularities)):
    val = i / len(angular_simularities)
    y_values.append(val)

count = 0
for i in range(len(angular_simularities)):
    if angular_simularities[i] > .75:
        count += 1
print(count)

plt.xlabel("angular simularities")
plt.ylabel("porportion of angular simularity with that value")
plt.title("angular simularity")
plt.plot(angular_simularities, y_values)
plt.show()



