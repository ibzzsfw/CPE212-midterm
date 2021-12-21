import time
import numpy as np
import pandas as pd

import algorithm_F
import algorithm_G


def rand(n):
    randomlist = np.random.choice(200000, n, replace=True)
    return randomlist


loop = 100
for j in range(0, 7):

    R = rand(10 ^ (j + 1))
    f = g = 0
    F = []
    G = []
    for i in range(100):
        t_F = time.time()
        algorithm_F.algorithmF(R)
        res_F = time.time()
        F.append(res_F - t_F)

        t_G = time.time()
        algorithm_G.algorithmG(R)
        res_G = time.time()
        G.append(res_G - t_G)
    