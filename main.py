

entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(entradas, pesos):
    soma = 0
    for i in range(3):
        # print(entradas[i])
        # print(pesos[i])

        soma += entradas[i] * pesos[i]
    return soma

def stepFuction(soma):
    if soma >= 1:
        return 1
    return 0

s = soma(entradas, pesos)

print(s)

r = stepFuction(s)

print(r)