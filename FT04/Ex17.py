print ("Vão-lhe ser pedidos 20 números reais.\n")

soma=0
média=1

for i in range(1, 21):
    num=float(input(f"Insira o {i}º número real:\t"))
    soma+=num

print(f"A soma dos números introduzidos é {soma} e a média é {soma/20}.")