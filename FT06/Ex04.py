"""
Efetua um programa em python que:
a. Imprima a quantidade de inteiros, floats, strings e boleanos na lista;
b. Efetua a média de todos os valores inteiros na lista.
c. Crie e retorne uma nova lista só com os valores inteiros
"""
print("Alínea a:")

nums=[10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]
inteiros=[]
quant_int = 0
quant_float = 0
quant_string = 0
quant_bool = 0

for elemento in nums:
    if type(elemento) == bool:  # Verifica se é um booleano
        quant_bool += 1
    elif type(elemento) == int:  # Se a divisão por 1 não tiver resto, é um inteiro
        quant_int += 1
        inteiros.append(elemento)
    elif type(elemento) == float:  # Se multiplicar por 0 não der erro, é um número (float)
        quant_float += 1
    else:  # Se não for número nem booleano, então é string
        quant_string += 1

print(f"Quantidade de inteiros: {quant_int}")
print(f"Quantidade de floats: {quant_float}")
print(f"Quantidade de strings: {quant_string}")
print(f"Quantidade de booleanos: {quant_bool}")

print("Alínea b:")

# b) Média dos inteiros


print(f"Média dos inteiros: {sum(inteiros)/len(inteiros)}")

print("Alínea c:")

print(f"Lista apenas com inteiros: {inteiros}")