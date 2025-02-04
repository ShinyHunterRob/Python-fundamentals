print ("Calculadora em Python")
num1= float(input("Insira o primeiro número: "))
num2= float(input("Insira o segundo número: "))

operacao = input("Insira a operação (+, -, *, /): ")

match operacao:
    case "+":
        result=num1+num2; print(f"O resultado é : {result}")
    case "-":
        result=num1-num2; print(f"O resultado é : {result}")
    case "*":
        result=num1*num2; print(f"O resultado é : {result}")
    case "/":
        if num2==0:
            print("Não é possível dividir por zero")
        else:
            result=num1/num2; print(f"O resultado é : {result}")
    case _:
        print("Operação inválida")
