'''Write a program(function!) that takes a list 
and returns a new list that contains all the elements of the first list 
minus all the duplicates.

Extras:

Write two different functions to do this 
- one using a loop and constructing a list, and another using sets.
- Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''

lista = [1, 2, 3, 4, 5, 5, 4, 3, 2,]

# Usando sets:

def filtro2(x):
    return(list(set(x)))

print(filtro2(lista))

# Usando loop e lista:

def filtro1(x):
    y = []
    for item in x:
        if item not in y:
            y.append(item)
    return y
print(filtro1(lista))
