import numpy as np

entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def soma(entradas, pesos):
    return entradas.dot(pesos)

def stepFuction(soma):
    if soma >= 1:
        return 1
    return 0

s = soma(entradas, pesos)

print(s)

r = stepFuction(s)

print(r)