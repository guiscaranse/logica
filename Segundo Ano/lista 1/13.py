hora_t = int(input("Insira as horas normais trabalhadas: "))
hora_e = int(input("Insira as horas extras trabalhadas: "))
bruto = float(hora_t*10 + hora_e*15)
print("Salário bruto: R$", bruto)
print("Salário líquido: R$", bruto - ((bruto/100)*10))