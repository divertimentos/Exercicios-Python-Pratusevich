import random

'''
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, 
they have a “cow”. 
For every digit the user guessed correctly in the wrong place 
is a “bull.” 

Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. 

Keep track of the number of guesses the user makes throughout the game 
and tell the user at the end.
'''
# Gerando 4 números aleatórios:
lista = []

for i in range(0, 4):
    sort = random.randint(0, 9)
    lista.append(sort)

while True:
    print(f"Lista gerada pelo computador: {lista}")
    # Pedindo número e trasnformando a string em lista:
    user = input("Adivinhe os 4 números: \n")
    listuser = list(user)
    listuser = list(map(int, listuser))  # Convertendo em integers os str dentro de listuser

    # Declarando e zerando contadores
    cow = bull = counter = 0

    # Encontrando bulls:
    for i in lista:
        for j in listuser:
            if j == i:
                bull += 1
    print(f"Bulls: {bull}")

    #  Encontrando cows:
    for i in lista:
        if i == listuser[counter]:
            cow += 1
        counter += 1
    print(f"Cows: {cow}")

    # Parando o programa:
    if cow == 4:
        print("Fim do programa.")
        break

# Esse programa tá super incompleto
# Porque eu não entendi completamente a explicação.
