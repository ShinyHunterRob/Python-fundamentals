num = int(input("Insira um número natural para calcular o seu factorial:\t"))

fatorial = 1
for i in range(1, num + 1):
    fatorial *= i

print(f"O fatorial de {num} é {fatorial}")

