menu={
    "entremeada": 7,
    "Sardinha": 6,
    "Filetes": 5.5,
    "Prego": 7,
    "Hamburguer": 5.5
}


#a. Devolva o preço do “prego”.
print(menu["Prego"])

#b. Faça o print de todas as chaves do dicionário
print(menu.keys())

#c. Acrescente na lista “omolete” com o preço de 5.
menu.update({"omolete":5})

#d. Faça o print de todo o dicionário, para visualizar as alterações.
print(menu)