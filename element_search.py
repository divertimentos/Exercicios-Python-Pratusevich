from random import randint
import timeit

'''
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) 
and another number. 

The function decides whether or not the given number is inside the list
and returns (then prints) an appropriate boolean.

Extra: use binary search.
'''

print('''Descrição do programa:

Este programa irá te perguntar quantos números naturais você deseja gerar.
Em seguida, ele irá pedir para você checar se um número natural pertence à lista.
O programa utilizará dois algoritmos diferentes, então você o verá rodar duas vezes. \n''')

# ========== Início do Programa ========== #

lista = []  # Cria uma lista vazia.
amount = int(input("Digite quantos números naturais você deseja gerar: \n"))

for i in range(amount):
    lista.append(randint(1, amount))  # Inserindo valores aleatórios na lista.


while True:
    generate = str(input("Deseja mostrar a lista? [S/N]: \n")).strip().upper()
    if generate[0] == "S":
        print(f"Lista gerada A: {lista} \n")
        break
    elif generate[0] == "N":
        print("Você decidiu não mostrar a lista. \n")
        break
    else:
        print("Por favor, digite apenas 'S' ou 'N'.")

# ========== Parte 1: busca clássica ========== # 

n = int(input('''Esta é a busca normal! 
Descubra se um número inteiro está na lista: \n'''))

def finder(lista, n):
    if n in lista:
        return True
    else:
        return False

finder(lista, n)  # Chamando a função com os dois parâmetros.

if finder(lista, n) == True:  # Se a função retornou True:
    print(f"O número {n} está na lista! \n")
elif finder(lista, n) == False:  # Se a função retornou False:
    print(f"O número {n} não está na lista! \n")

print("= * =" * 15)

# ========== Parte 2: laço inteligente ========== # 

listb = []  # Declarando uma nova lista B
for j in range(amount):
    listb.append(randint(1, amount))  # Inserindo valores aleatórios na lista.

if generate[0] == "S":
    print(f"Lista gerada B: {listb}")

n = int(input('''\nEsta é a busca inteligente! 
Descubra se um número inteiro está na lista: \n'''))

def smartfinder(listb, n):  # Definindo a função.
    
    while len(listb) >= 0:  # Enquanto houver itens na lista, rode:
        mid_len = len(listb) // 2  # mid_len é o índice que está na metade da lista atual
        middle_element = listb[mid_len]  # Item que está na metade da lista
        
        if n == middle_element:  # Quando n for o item central,
            return True  # Retorne True e saia do while
        else:
            if n < middle_element:  # Se n estiver à esquerda do meio,
                listb = listb[0: mid_len]  # Lista B vai de listb[0] até o meio atual
            elif n > middle_element:  # Se n estiver à direita do meio,
                listb = listb[mid_len:]  # Lista B vai do meio de listb até o último índice.
        
        if len(listb) == 1:  # Quanto e se a lista alcançar 1 item
            if n != listb[0]:  # E se esse item for diferente de n:
                return False  # Significa que n não pertence à lista

smartfinder(listb, n)  # Chamando a função com seus 2 parâmetros.

if smartfinder(listb, n) == True:
    print(f"O número {n} está na lista.")
elif smartfinder(listb, n) == False:
    print(f"Número {n} não está na lista.")
