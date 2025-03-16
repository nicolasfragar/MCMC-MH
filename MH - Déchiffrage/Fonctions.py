import numpy as np

# Création de la liste des caractères uniques

alphabet = "abcdefghijklmnopqrstuvwxyzàâçèéêëîïñôùûü '."

# Calibrage

def nettoie(tref):
    chars = []
    tref = tref.lower()
    for i in tref:
        if i == "\n":
            chars.append(" ")
        #elif i == " ":
        #    chars.append(" ")
        elif i in alphabet:
            chars.append(i)
    return "".join(chars)

def compteur(tref):
    freq = {}
    for i in range(len(tref)-1):
        if tref[i] in alphabet and tref[i+1] in alphabet:
            if tref[i]+tref[i+1] in freq:
                freq[tref[i]+tref[i+1]] += 1
            else:
                freq[tref[i]+tref[i+1]] = 1
    return freq

# Chiffrage

def check(code):
    for i in code:
        if i not in alphabet:
            return False
    for i in alphabet:
        if i not in code:
            return False
    else:
        return True

def encode(code, str):
    new_str = []
    for i in str:
        if i in alphabet: 
            new_str.append(code[alphabet.index(i)])
        elif i == " ":
            new_str.append(" ")
    return "".join(new_str)

def decode(code, str):
    new_str = []
    for i in str:
        if i in code:
            new_str.append(alphabet[code.index(i)])
        elif i == " ":
            new_str.append(" ")
    return "".join(new_str)

def code():
    code = list(alphabet) #list(alphabet[0:-3])
    np.random.shuffle(code)
    code.append(" '.")
    return "".join(code)

# Score

def score(texte, code, freq):
    score = 0
    texte = decode(code, texte)
    for i in range(len(texte)-1):
        if texte[i] + texte[i+1] in freq:
            score += np.log(freq[texte[i] + texte[i+1]])
    return score

# Propositions

def proposition(code):
    code = list(code)
    i, j = np.random.randint(0, len(code), 2)#np.random.randint(0, len(code)-3, 2)
    code[i], code[j] = code[j], code[i]
    return "".join(code)