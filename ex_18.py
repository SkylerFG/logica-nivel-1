#Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

n1=int(input("Diga o primeiro número: "))
n2=int(input("Diga o segundo número: "))
n3=int(input("Diga o terceiro número: "))
if n1 > n2 and n3 > n2:
    soma = n1 + n3
elif n2 > n1 and n3 > n1:
    soma= n2 + n3
else:
    soma = n1 + n2
print ("O resultado da soma entre os dois maiores números é:", soma)
