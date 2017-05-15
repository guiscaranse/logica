'''
Este programa foi um pouco mais elaborado do que a proposta
Ele permite cadastrar novos feriados e novos meses em uma lista.
Como funciona? Simples, adicione o nome, dia e o mês na mesma posição das três listas
O programa vai verificar se o mês e o dia estão dentro da lista, e verificará se o dia e o mês estão na mesma posição (feriado)
'''
nomes_feriados = ["1 de janeiro (confraternização universal)", "21 de abril (Tiradentes)", "1 de maio (dia do trabalho)", "7 de setembro (independência do Brasil)", "12 de outubro (Nossa Senhora Aparecida, padroeira do Brasil)", "2 de novembro (Finados)", "15 de novembro (proclamação da república)", "25 de dezembro (natal)"]
dias_feriados =  [1, 21, 1, 7, 12, 2, 15, 25]
meses_feriados = [1, 4, 5, 9, 10, 11, 11, 12]
dia = int(input("Insira o dia a ser conferido: "))
mes = int(input("Insira o mês a ser conferido: "))
feriado = None
if(dias_feriados.count(dia) > 0 and meses_feriados.count(mes) > 0):
    for (i, dia_f) in enumerate(dias_feriados):
        if(dia_f == dia):
            for (l, mes_f) in enumerate(meses_feriados):
                if(mes_f == mes):
                    if (l == i):
                        feriado = nomes_feriados[l]
if feriado != None:
    print("Feriado: ", feriado)
else:
    print("Dia normal!")
