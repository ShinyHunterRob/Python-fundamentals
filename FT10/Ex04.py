Txt="""Python é uma linguagem de programação
3 de 3
de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""

"""
Escreve um programa em Python que
a. Imprima o texto anterior todo em maiúsculas;
b. Peça uma palavra ao utilizador e verifique se a mesma está ou não no texto, devolvendo o resultado ao utilizador.
c. Imprima o número de vezes que a letra ‘O’ ocorre no texto
d. Substitua todaa as ocorrências da letra ‘P’ no texto por ‘_
"""


print(Txt.upper())

word=input("Insira uma palavra para verificar se ela se encontra na frase: \t")

if word in Txt:
    print("A palavra inserida está na frase.")
else:
    print("A palavra inserida não está na frase.")

print(Txt.count("o"))

print(Txt.replace("p","_"))