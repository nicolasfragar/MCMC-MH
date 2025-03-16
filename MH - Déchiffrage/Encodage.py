from Fonctions import *

# Importe le secret qu'on veut décoder
secret = open("secret.txt", "r")
secret_ = "".join([line for line in secret])
secret.close()

secret = nettoie(secret_)

# Encodage du secret
code = code()
secret = encode(code, secret)

# Écriture du secret encodé dans un nouveau fichier
with open("secret_encodé.txt", "w") as encoded_file:
    encoded_file.write(secret)

