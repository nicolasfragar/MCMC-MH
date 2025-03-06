import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import time

#### Paramètres ####
N = 100000
max_iter = 40
Sigma = np.array([[1, 0], [0, 1]])

#### Fonctions ####

def in_mandelbrot(z):
    res = 0
    for i in range(max_iter):
        res = res * res + z
        if res.real * res.real + res.imag * res.imag > 4:
            return 0
    return 1

def MH_A(x, prop, var_x, var_prop):
    res = min(1, ((in_mandelbrot(prop) * var_x) / (in_mandelbrot(x) * var_prop)))
    return res

def MH_markov(x, Sigma):
    u = np.random.uniform(0, 1)
    prop_real_imag = np.random.multivariate_normal([x.real, x.imag], Sigma)
    prop = complex(prop_real_imag[0], prop_real_imag[1])
    var_x = multivariate_normal(mean=[x.real, x.imag], cov=Sigma).pdf([x.real, x.imag])
    var_prop = multivariate_normal(mean=[x.real, x.imag], cov=Sigma).pdf([prop.real, prop.imag])
    if u < MH_A(x, prop, var_x, var_prop):
        return prop
    else:
        return x

#### Main Script ####
start_time = time.time()  # Record the start time

L = np.zeros((2, N + 1))
for i in range(1, N + 1):
    z = complex(L[0, i-1], L[1, i-1])
    z = MH_markov(z, Sigma)
    L[0, i] = z.real
    L[1, i] = z.imag

end_time = time.time()  # Record the end time
elapsed_time = end_time - start_time  # Calculate the elapsed time
print(f"Computation Time: {elapsed_time:.2f} seconds")  # Print the elapsed time

#### Représentation ####
fig, ax = plt.subplots()
ax.scatter(L[0], L[1], s=0.1, color='black')
plt.show()

