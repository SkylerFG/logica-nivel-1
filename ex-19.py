 #Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

n1=int(input("Diga o primeiro número: "))
n2=int(input("Diga o segundo número: "))
n3=int(input("Diga o terceiro número: "))
if n1 < n2 and n1 < n3:
    if n2 < n3:
        print (n1, n2, n3)
    else:
        print (n1, n3 ,n2)
elif n3 < n1 and n3 < n2:
    if n1 < n2:
        print (n3, n1, n2)
    else:
        print (n3, n2, n1)
elif n2 < n1 and n2 < n3:
    if n1 < n3:
        print (n2, n1, n3)
    else:
        print (n2, n3, n1)
