num = int(input("Insira um número inteiro, que vou fazer uma coisa gira.\t"))

# Usando for para a sequência crescente
elemento_crescente = 1
for i in range(num, 0, -1):
    print(f"{elemento_crescente} - {i}")
    elemento_crescente += 1
