dia = int(input("Insira o dia: "))
mes = int(input("Insira o mês: "))
ano = int(input("Insira o ano: "))
if dia <= 31 and dia > 0 and mes > 0 and mes < 12 and ano > 0:
    print ("Data válida!")
else:
    print("Data inválida!")
