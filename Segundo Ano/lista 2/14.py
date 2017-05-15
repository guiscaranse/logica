# Questão duplicada :P
numeros = []
# Inicia uma lista que armazenará os 3 números
# A função "append" insere o valor dentro de nossa lista
numeros.append(int(input("Insira um número (1/3): ")))
numeros.append(int(input("Insira um número (2/3): ")))
numeros.append(int(input("Insira um número (3/3): ")))
numeros.sort(reverse=True)
# A função sort organiza os números, por padrão ela organiza eles em ordem crescente, então indicando pelo argumento reverse ela os imprimirá em ordem decrescente
print("Números em ordem decrescente: ", numeros)
