import math as m
import random as r
import numpy as np
from numpy import log as ln
from numpy import linalg as LA
import matplotlib.pyplot as plt


n = 500
d = 100

def s_ang(a, b):
    a = normalize(a)
    b = normalize(b)
    dot = np.dot(a, b)
    if (dot > 1): dot = m.floor(dot)
    return 1 - (1/m.pi) * np.arccos(dot)

def normalize(v):
    vector_norm = LA.norm(v, 2)
    for i in range(len(v)):
        v[i] = v[i] / vector_norm
    return v

r = open("R.txt", "r").read()

vectors = r.split("\n")[0:500]
for i in range(len(vectors)):
    vectors[i] = vectors[i].split()
    for j in range(len(vectors[i])):
        vectors[i][j] = float(vectors[i][j])


angular_simularities = []
for i in range(len(vectors)):
    for j in range(i + 1, len(vectors)):
        simularity = s_ang(vectors[i], vectors[j])
        angular_simularities.append(simularity)

angular_simularities.sort()
print(len(angular_simularities))

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



