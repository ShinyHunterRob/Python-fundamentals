num = int(input("Insira um número natural para calcular a soma dos números naturais até ele:\t"))

soma=0
for i in range(1,num+1,1):
    soma+=i
    print(soma)