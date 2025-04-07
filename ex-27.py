#25) Somar números positivos digitados pelo usuário até que ele digite um número negativo

print("Somador de números positivos, digite um número negativo para terminar a conta")
soma=0
numero=0
while numero >= 0:
    numero=int(input("Digite outro número: "))
    if numero < 0:
        break
    else:
     soma += numero
print (soma)
