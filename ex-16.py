# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

maca=float(input("Quantas maças foram compradas? "))
if maca >= 12:
    valor=1*maca
else:
    valor=1.30*maca
print ("Voçê irá pagar:", valor)
