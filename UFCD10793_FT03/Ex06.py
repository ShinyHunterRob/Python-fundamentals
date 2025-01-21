num1 = int(input("Insira o primeiro número:\t"))
num2 = int(input("Insira o segundo número:\t"))
num3 = int(input("Insira o terceiro número:\t"))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} é o maior número.")
    else:
        print(f"{num3} é o maior número.")
elif num2 > num3:
    print(f"{num2} é o maior número.")
else:
    print(f"{num3} é o maior número.")

#AND
if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior número.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é o maior número.")