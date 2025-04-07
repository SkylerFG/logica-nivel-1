#26) Ler 5 números digitados pelo usuário e armazenar em um vetor. Depois, imprime os números informados.

vetor_numeros = []
for i in range(5):
    ndigitado=int(input("Digite um número: "))
    vetor_numeros.append(ndigitado)
print(vetor_numeros)
