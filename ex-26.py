#24) Pedir senha até que seja digitada a correta

senha = 12345
digitado=int(input("Digite sua senha: "))
while digitado != senha:
    print ("Senha errada, tente novamente!")
    digitado=int(input("Digite sua senha: "))
print ("Senha correta!")
