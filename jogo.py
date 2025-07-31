import random
print("##################################################################")
print("#       Jogo de adivinhação                                     # ")
print("#              ❤️‍🩹Loirinha❤️‍🩹                                     # ")
print("##################################################################")
print("                     ❤️‍🩹                                           ")

numeroSecreto= random.randrange (0,100)
totalTentativas = 0
pontos = 100

print("qual niveis de dificuldade?")
print("(1)- fácil (2)- médio (3)- difícil ")

nivel = int(input("Escolha um nível "))

if(nivel == 1):
    print(" 20 tentativas")
if(nivel == 2 ):
    print(" 10 tentativas")
    totalTentativas = 10 
elif(nivel == 3):
    print("5 tentativas")
    totalTentativas = 5
    

