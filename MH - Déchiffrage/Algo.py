from Fonctions import *
import numpy as np

# Importe le texte de référence, ici : Les misérables de Victor Hugo
les_mis = open("Les miserables.txt", "r")
lines = "".join([line for line in les_mis])
les_mis.close()

# Calcul des fréquences
lines = nettoie(lines)
freq = compteur(lines)

"""# Importe le secret qu'on veut décoder
secret = open("secret.txt", "r")
secret_ = "".join([line for line in secret])
secret.close()

secret = nettoie(secret_)

# Encodage du secret
code = code()
secret = encode(code, secret)"""

secret = open("secret_encodé.txt", "r")
secret_ = "".join([line for line in secret])
secret.close()
secret = secret_

# Implementation de l'algorithme
f0 = "abcdefghijklmnopqrstuvwxyzàâçèéêëîïñôùûü '."
N = 10000

f = f0
f_score = score(f, freq, secret)
for i in range(N):
    T = 1
    f_prop = proposition(f)
    f_prop_score = score(secret,f_prop, freq)
    u = np.random.uniform()
    if np.log(u) < (f_prop_score - f_score):
        f = f_prop
        f_score = f_prop_score
    print(f"Itération n°{i+1} : {decode(f, secret)[0:168]}")

decodé = decode(f, secret)
print(f"Estimation finale : {decodé}")