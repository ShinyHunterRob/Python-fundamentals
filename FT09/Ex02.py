"""
a. Cries um dicionário e efetues o respetivo print.
b. Acrescentes dois novos elementos ao dicionário.
c. Removes um dos elementos da lista;
d. Efetues uma operação, à escolha, sobre os dados no dicionário
"""

notas = {
    "Português": 14,
    "Inglês": 12,
    "Francês": 16
}

print(notas)

notas.update(
    {
        {"Espanhol":10},
        {"Alemão": 8}
    }
)

notas.pop("Alemão")

notas["Espanhol"]=16