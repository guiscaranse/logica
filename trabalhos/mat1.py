count = int(input("Quantas linhas deve gerar? "))
a = 1
b = 1
linhas = []
# Gerar a matriz do triângulo
while (a <= count):
    colunas = []
    b=1
    while(b <= a):
        colunas.append(0)
        b+=1
    linhas.append(colunas)
    a+=1
a = 0
# Insere '1' na primeira coluna
while (a < count):
    linhas[a][0] = 1
    linhas[a].append(0)
    a+=1
a = 0
######
print(linhas)
print(len(linhas[2]))
while(a < count):
    print(a, "M")
    b = 0
    while(b < a):
        print(b, "S")
        linhas[a+1][b+1] = linhas[a][b] + linhas[a][b+1]
        b+=1
    a+=1
