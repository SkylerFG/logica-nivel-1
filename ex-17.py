#Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

n1=int(input("Diga o primeiro número: "))
n2=int(input("Diga o segundo número: "))
n3=int(input("Diga o terceiro número: "))
if n1 > n2 and n1 > n3:
    nm=n1
elif n2 > n1 and n2 > n3:
    nm = n2
else:
    nm = n3
print ("O maior número é o ", nm)
