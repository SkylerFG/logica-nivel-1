#Verificação de Nota - Peça ao usuário para digitar sua nota (0 a 10) e classifique:
#Nota ≥ 7: Aprovado
#Nota entre 5 e 6.9: Recuperação
#Nota < 5: Reprovado

nota=float(input("Diga sua nota: "))
if nota >= 7:
    print ("Você está aprovado")
elif nota <= 6.9 and nota > 5:
    print ("Você está de recuperação")
else:
    print ("Você está reprovado")
