"""
Cria um programa, em python, que:
a. Indique quantas pessoas são menores de idade
b. Ordene a lista por ordem decrescente
c. Pede ao utilizador uma idade e verifica se essa idade está na lista.
#- Se estiver faz print("A idade está na lista")
#- Caso contrário faz o print("não existe ninguém com essa idade na lista")
"""

idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]

idades.count(sum(1 for idade in idades if idade < 18))

idades.sort(reverse=True)
print(idades)

idade_pedida=int(input("Insira um número para verificar se existe na lista: "))
if idade_pedida in idades:
    print("A idade está na lista")
else:
    print("Não existe ninguém com essa idade na lista")