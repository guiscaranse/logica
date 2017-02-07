import math
count = int(input("Quantas linhas você quer? "))

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
    for a in range(len(triangulo)):
        print(" ", a, end="")
    # Escreve as linhas do triângulo
    print('')
    for linha in triangulo:
        linha = str(linha).replace("[", "")
        linha = str(linha).replace("]", "")
        print(" ", linha)
pascal(gerador_pascal(count))
print()
