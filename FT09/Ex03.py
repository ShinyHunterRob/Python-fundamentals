#Efetua um programa em python:
#a. Instancie o seguinte dicionário:
Computadores_1={
    "Marca":"Asus",
    "Ecra":"14Pol",
    "RAM": [4, 8, 12]
}

# Acrescente um novo elemento à lista com chave igual a “Disco” e valor [“128G”, “256G”]
Computadores_1.update({"Disco":["128G", "256G"]})

#c. Permita ao utilizador introduzir um valor específico de RAM e verificar se esta está presente na lista.
chave= input("Insira o nome da chave a inserir:\t")
valor=input("Insira o valor da chave a inserir:\t")

#d. Acrecente 16 como novo valor de RAM.
Computadores_1.update(
    {"RAM":[4, 8, 12, 16]}
)

#e. Copie o dicionário para um novo usando Deep Copy().
Computadores_2=Computadores_1.copy()

#f. Na lista nova modifique a marca para “Lenovo” e os valores da RAM para [4,8]. Imprima a nova lista
Computadores_2.update(
    {"Marca":"Lenovo"}
)

Computadores_2.update(
    {"RAM": [4, 8]}
)

print(Computadores_2)

#g. Crie uma nova lista com deep copy e modifique a marca para “HP” e Disco para [“256G”]- Imprima a respetiva lista
Computadores_3=Computadores_1.copy()
Computadores_3.update(
    {"Marca":"HP"}
)

Computadores_3.update(
    {"Disco": ["256G"]}
)

print(Computadores_3)

#h. Cria uma lista cujos elementos são os três dicionários.
lista=list((Computadores_1, Computadores_2, Computadores_3))

#i. Imprima as marcas com 128G de Disco
for i in lista:
    if "128G" in i["Disco"]:
        print(i["Marca"])

#j. Imprima as marcas com 8 e 12 de RAM

for i in lista:
    if 8 and 12 in i["RAM"]:
        print(i["Marca"])
