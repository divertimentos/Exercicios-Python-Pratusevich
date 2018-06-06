'''
Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements 
of the given list. 
For practice, write this code inside a function.
'''

lista = [5, 10, 15, 20, 25]

def firstlast():
    listb = []
    listb.append(lista[0])
    listb.append(lista[-1])
    return print(f"Primeiro e último valores: {listb}")

firstlast()
