import re
print ("Este programa irá calcular em qual faixa do espectro sonoro a onda está.")
f_text = input("Por favor digite a frequência em Hz, Mhz, Khz, Ghz (Exemplo: 20Ghz): ")
# Extrai dígitos
f_valor = float(re.sub("\D", "", f_text))
# Extrai a unidade de medida de frequência
f_medida = "".join(re.findall("[a-zA-Z]+", f_text)).lower()
# Todas as medidas diferentes de Hz serão convertidas para Hz
def response(hz):
    # Script que indica o espectro
    if hz > 0 and hz <= 20:
        print("A frequência que você digitou é um infra-som!")
    elif hz > 20 and hz <= 20000:
        print("A frequência que você digitou é um som audível!")
    elif hz > 20000:
        print("A frequência que você digitou é um ultrasom!")
    else:
        print("Não foi possível identificar ):")
if f_medida == "ghz":
    f_valor = f_valor * 1e+9 # Hz
    response(f_valor)
elif f_medida == "khz":
    f_valor = f_valor * 1000
    response(f_valor)
elif f_medida == "mhz":
    f_valor = f_valor * 1000000
    response(f_valor)
elif f_medida == "hz":
    # Não precisa de conversão
    response(f_valor)
else:
    print("A medida de frequência é inválida!\nSó são aceitos:\n*Hz\n*Mhz*\n*Khz\n*Ghz")
