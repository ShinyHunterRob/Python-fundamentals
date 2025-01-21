lado1 = float(input("Insira a medida do primeiro lado do triângulo:\t"))
lado2 = float(input("Insira a medida do segundo lado do triângulo:\t"))
lado3 = float(input("Insira a medida do terceiro lado do triângulo:\t"))

if lado1==lado2==lado3:
    print("O triângulo é equilátero.")
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")