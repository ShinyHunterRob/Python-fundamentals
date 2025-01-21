nome = input("Insira o seu nome:\t")
idade = int(input("Insira a sua idade:\t"))
peso = float(input("Insira o seu peso:\t"))
altura = float(input("Insira a sua altura:\t"))

imc = peso/(altura*altura)

if imc < 17:
    print("Muito abaixo do peso ideal")
elif imc < 18.5:
    print("Abaixo do peso ideal")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print ("Acima do peso ideal")
elif imc < 35:
    print ("Obesidade grau I")
elif imc < 40:
    print ("Obesidade grau II")
else:
    print ("Obesidade grau III")