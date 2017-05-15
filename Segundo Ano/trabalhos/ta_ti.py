from itertools import chain
dados = [[420, 22, 6.8, 50], [421, 26, 6.8, 70], [430, 27, 9.8, 70], [431, 33, 9.9, 70], [440, 34, 10, 100], [500, 23, 14, 70], [501, 31, 10, 70], [502, 43, 14, 100],
         [510, 33, 10, 100], [511, 46, 14, 120], [520, 49, 15, 150], [521, 70, 22, 170], [522, 94, 34, 230], [530, 79, 22, 220], [531, 110, 34, 250], [532, 140, 52, 400]]
# 0 = Combinação, 1 = Índice de MNP/100ml, 2 = Limites inferior com 95% de confiabilidade, 3 = Limites superiores com 95% de confiabilidade
def busca(lista, objeto):
    '''
    @desc Função responsável por buscar a primeira ocorrência em listas multidimensionais para pegar a posição da lista contendo o objeto
          visto que o 'if in()' não detecta objetos dentro de listas multidimensionais e apenas a camada mais externa é atingida.
    @param list lista - lista a ser procurada
    @param string objeto - o objeto a ser procurado na lista
    @return integer lista.index() - a posição da lista
    '''
    x = [x for x in lista if objeto in x][0]
    return lista.index(x)
d = chain(*dados)
s = str(input("Insira o número do PRIMEIRO tubo positivo: "))
s += str(input("Insira o número do SEGUNDO tubo positivo: "))
s += str(input("Insira o número do TERCEIRO tubo positivo: "))
if int(s) in d:
    print("A combinação de tubos informada foi:", s)
    print("O índice de MNP/100ml é %s!" %(dados[busca(dados, int(s))][1]))
    print("Isso significa que 95%%, das amostras de água, contém entre %s e %s bactérias! Com %s sendo o número mais provável" %(dados[busca(dados, int(s))][2], dados[busca(dados, int(s))][3], dados[busca(dados, int(s))][2]))
else:
    print("Banana")
