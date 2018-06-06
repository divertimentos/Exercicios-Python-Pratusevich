# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

while True:
    print("Digite: 'Pedra', 'Papel' ou 'Tesoura' para jogar.")

    player1 = input("Jogador 1: \n")
    player2 = input("Jogador 2: \n")

    if player1 == "pedra" and player2 == "papel":
        print("Papel vence pedra. Jogador 2 ganhou.")
    elif player1 == "pedra" and player2 == "tesoura":
        print("Pedra vence tesoura. Jogador 2 venceu.")
    elif player1 == player2:
        print("Empate.")
again = input("Jogar novamente? SIM / NÃO")


# Neste exercício, a resposta requer importação de funções e 
# eu ainda não conheço nada disso do Python. 
# Ele importa um "sys". Porra.
