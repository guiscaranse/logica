taxa_estados = ["BA", "SP", "RJ", "MS"]
taxa_valor =   [17, 12, 15, 8]
estado = str(input("Insira a sigla do estado: ")).upper()
if taxa_estados.count(estado) == 0:
    print("Estado não encontrado ou não possui impostos!")
else:
    valor = float(input("Insira o valor do produto : R$"))
    print("Novo valor acrescido de impostos: R$", valor + (valor/100*taxa_valor[taxa_estados.index(estado)]))
