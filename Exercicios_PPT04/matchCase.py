print ("Temos á venda vários produtos:\n")
print ("Smartphones, Tablets, Laptops, Outros")

produto = input("Escreva o nome do produto: ").strip().lower()
preco = float(input("Escreva o preço do produto: "))

desconto = 0

match produto:
    case "smartphone":
        desconto = 0.10
    case "tablet":
        desconto = 0.15
    case "laptop":
        desconto = 0.20
    case _:
        desconto = 0

preco_final = preco * (1 - desconto)
print(f"O preço final do {produto} com desconto é: € {preco_final:.2f}")