import math, os, sys
from colorama import *
init(autoreset=True)

count = int(input("Quantas linhas você quer? "))
print(Back.RED + "Gerando triângulo de pascal!")
def combinacoes(n, p):
    return [sum(par) for par in zip(n, p)]

def gerador_pascal(linhas):
    resultados = []
    for pos in range(linhas):
        # Inicia com o primeiro '1' do triângulo
        linha = [1]
        if resultados:
            # Para se referir a última linha
            u_linha = resultados[-1]
            # Pega a próxima combinação levando em consideração que o zip irá somar em pares sempre em formato de "escorregador"
            # Coletando a última combinação e somando com a próxima
            # Exemplo: [1, 1]
            # Ele irá somar, armazenar a próxima combinação (2) e passar para a próxima casa, como se fosse um escorregador
            linha.extend(combinacoes(u_linha, u_linha[1:]))
            # Adiciona o '1' no final
            linha.append(1)
        resultados.append(linha)
    return resultados

def pascal(triangulo):
    print("  ", end="") # Ajusta posição dos ids
    for a in range(len(triangulo)): # Faz uma régua para colunas
        print(" ", a, end="")
    # Escreve as linhas do triângulo
    print("")
    x = 0
    for linha in triangulo:
        linha = str(linha).replace("[", "").replace("]", "") # Remove []
        print(x, "|", linha) # Indica a linha e printa a linha do triangulo
        x += 1



def pascal_linhas(triangulo, linha):
    if linha > (len(triangulo) - 1):
        sys.exit(Back.RED + "Coordenadas inválidas!")
    print(Fore.RED + "Mostrando relação da linha:", "[", linha, "]")
    x = 0
    for linhas in triangulo:
        linhas = str(linhas).replace("[", "").replace("]", "") # Remove []
        if((x+1) == linha):
            print(Back.GREEN + "2^" + str(x), "|", Back.GREEN + linhas) # Indica a linha e printa a linha do triangulo
        else:
            print("2^" + str(x), "|", linhas) # Indica a linha e printa a linha do triangulo
        x += 1
pascal(gerador_pascal(count))
l = int(input("Escolha a linha do objeto: "))
os.system("cls")
pascal_linhas(gerador_pascal(count), l)
