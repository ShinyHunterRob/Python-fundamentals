num1 = int(input("Insira um número inteiro:\t"))
num2 = int(input("Insira outro número inteiro:\t"))

if num1 == num2:
    print("Os números inseridos são iguais")
elif num1 > num2:
    print(f"{num1} é maior que {num2}")
else:
    print(f"{num1} é menor que {num2}")