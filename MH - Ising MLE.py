# Importation
import numpy as np

# Paramètres
L = np.random.choice([1, -1], (6, 6))
theta = np.array([1, 1])
phi = np.array([0, 1])


# Fonctions
def H(L, theta):
    """Hamiltonien de L selon le paramètre theta, il sert a calculer les probas de transition"""
    t1 = np.sum(L)
    t2 = 0
    # On parcourt un spin sur deux pour éviter de compter deux fois les interactions et on somme les produits des spins voisins
    for i in range(int(L.shape[0]/2)):
        i = 2*i
        for j in range(int(L.shape[1]/2)):
            j = 2*j
            t2 += L[i, (j+1) % len(L)] * L[i, j] + L[i, (j-1) % len(L)] * L[i, j] + L[(i+1) % len(L), j] * L[i, j] + L[(i-1) % len(L), j] * L[i, j]
    return theta[0] * t1 + theta[1] * t2

def p_switch(i, j, theta, L):
    """La probabilité de changer un spin"""
    L_prime = L.copy()
    L_prime[i, j] = -L_prime[i, j]
    return np.exp(H(L_prime, theta) - H(L, theta))  #Exponentielle de la différence des Hamiltoniens (différence d'énergie)

def MH_markov(L, theta):
    """Algorithme de Metropolis-Hastings pour la chaine de Markov qui sert d'échantillonneur pour z_n"""
    L_prime = L.copy()
    # Pour chaque spin on tente de changer de lui changer le signe avec probabilité p_switch
    for i in range(len(L_prime)): 
        for j in range(len(L_prime[i])):
            u = np.random.uniform(0, 1) 
            r = p_switch(i, j, theta, L_prime) 
            if u < r:
                L_prime[i, j] = -L_prime[i, j]
    # Comme dans Geyer, on tente de faire une symétrie pour parcourir tout l'espace (symetry swap dans Geyer)
    u = np.random.uniform(0, 1)
    r = np.exp(H(-L_prime, theta) - H(L_prime, theta))
    if u < r:
        L_prime = -L_prime
    return L_prime

def z_n(theta, n):
    """Estimateur de z_n, la constante de normalisation de la loi"""
    z_n = 0
    # On échantillonne z_n par la chaine de Markov
    S = np.zeros((n, L.shape[0], L.shape[1]))
    S[0] = L.copy()
    for i in range(1, n):
        S[i] = MH_markov(S[i-1], theta)
    # On calcul la somme des rapports des vraisemblances non normalisées (comme dans Geyer)
    for i in S:
        z_n += np.exp(H(i, theta))/np.exp(H(i, phi))
    return z_n/n

def l(theta, phi, L, z_n):
    """Le log du rapport des vraisemblances de phi et theta"""
    return np.log(np.exp(H(L, theta))/np.exp(H(L, phi))) - np.log(z_n)

# Test
zn_value = z_n(theta, 1000)
l_value = l(theta, phi, L, zn_value)

# Il reste encore à trouver le maximum de cette fonction qu'on est capable de calculer
