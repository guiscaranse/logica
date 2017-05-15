altura = float(input("Insira a sua altura: "))
sexo = str(input("Insira o seu sexo [m/f]: "))

if sexo == "m" or sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal é: ", peso_ideal)
elif sexo == "F" or sexo == "f":
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é: ", peso_ideal)
else:
    print("Sexo inválido!")
