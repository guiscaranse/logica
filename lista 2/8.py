notas = []
notas.append(float(input("Insira uma nota (1/4): ")))
notas.append(float(input("Insira uma nota (2/4): ")))
notas.append(float(input("Insira uma nota (3/4): ")))
notas.append(float(input("Insira uma nota (4/4): ")))
if (sum(notas)/4) >= 6:
    print ("Passou!")
else:
    print ("Não passou!")
