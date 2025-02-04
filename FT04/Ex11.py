num = int(input("Insira um número natural para calcular a soma e o produto dos números naturais até ele:\t"))

soma=0
produto=1
for i in range(1,num+1,1):
    soma+=i
    produto*=i

print(f"Número: {num}\nSoma: {soma}\nProduto: {produto}")