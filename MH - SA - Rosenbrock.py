import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.stats import multivariate_normal

#### Paramètres ####
N = 10000
L = np.zeros((N+1, 2))
a = 1
b = 100
Sigma = np.array([[1, 0], [0, 1]])
n = 1

#### Fonctions ####
def p(x):
    return np.exp(-((a-x[0])**2 + b*(x[1]-x[0]**2)**2))

def Q(x):
    return np.random.multivariate_normal(x, Sigma)

def Q_densite(x):
    var = multivariate_normal(mean=x, cov=Sigma)
    return var.pdf(x)

def A(x, y, T, px, py):
    return (py**T * Q_densite(x)) / (px**T * Q_densite(y))

def cooling(i):
    return np.sqrt(i) if i >= 1 else 1

#### Algo ####
best = np.array([0, 0])
p_best = p(best)
for i in range(1, N+1):
    T = cooling(i)
    x = L[i-1]
    px = p(x)
    if px > p_best:
        best = x
        p_best = px
    u = np.random.uniform(0, 1)
    prop = Q(x)
    p_prop = p(prop)
    if u < A(x, prop, T, px, p_prop):
        L[i] = prop
    else:
        L[i] = x

#### Représentation ####
L = np.array(L)

fig, ax = plt.subplots()
ax.scatter(L.T[0][10:], L.T[1][10:], s=0.1, color='black')
ax.scatter(L[-1][0], L[-1][1], s=10, color='red')
ax.scatter([1], [1], s=10, color='blue')
ax.scatter([best[0]], [best[1]], s=10, color='green')
print(best)
plt.show()