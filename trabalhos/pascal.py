import math
count = int(input("Quantas linhas você quer? "))

def combinacoes(n, p):
    return int((math.factorial(n)) / ((math.factorial(p)) * math.factorial(n - p)))

def gerador_pascal(linhas):
    resultados = []
    for pos in range(linhas):
        linha = []
        for prox in range(pos+1):
            linha.append(combinacoes(pos, prox))
        resultados.append(linha)
    return resultados

def pascal(triangulo):
    for linha in triangulo:
        print(linha)
pascal(gerador_pascal(count))
