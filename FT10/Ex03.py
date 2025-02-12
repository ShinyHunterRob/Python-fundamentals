datas="12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"

"""
Escreve um programa em Python que
a. Armazene as diferentes datas numa string;
b. Imprima as datas correspondentes ao ano de 2022;
c. Crie uma noca lista (dias) e na mesma armazena o dia de cada uma das
datas. Ordene a lista de forma crescente e imprima a mesma.
"""

#a. Armazene as diferentes datas numa string;
datas_string="12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"

#b. Imprima as datas correspondentes ao ano de 2022;
datas_divididas=datas_string.split(",")

for i in datas_divididas:
    if i.endswith("2022")==True:
        print(i)

#c. Crie uma noca lista (dias) e na mesma armazena o dia de cada uma das datas. Ordene a lista de forma crescente e imprima a mesma.
dias = list()

for i in datas_divididas:
    dias.append(i[:2])
    dias.sort()

print(dias)