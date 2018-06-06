from datetime import datetime
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

currentyear = (datetime.now().year)
nome = input("Digite seu nome: \n")
idade = int(input("Digite sua idade: \n"))
birth = (currentyear - idade)

if idade < 100:
    print(f"Olá, {nome}! Você completará 100 anos no ano de {birth + 100}")
elif idade < 0:
    print(f"Olá, feto. Você ainda não nasceu.")
else:
    print(f"Olá, {nome}! Você completou 100 anos em {birth + 100}")
