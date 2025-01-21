print ("Calculadora em Python")
num1= float(input("Insira o primeiro número: "))
num2= float(input("Insira o segundo número: "))

operacao = input("Insira a operação (+, -, *, /): ")

if operacao=="+":
    result=num1+num2; print(f"O resultado é : {result}")
elif operacao=="-":
    result=num1-num2; print(f"O resultado é : {result}")
elif operacao=="*":
    result=num1*num2; print(f"O resultado é : {result}")
elif operacao=="/":
    if num2==0:
        print("Não é possível dividir por zero")
    else:
        result=num1/num2; print(f"O resultado é : {result}")
else:
    print("Operação inválida")
