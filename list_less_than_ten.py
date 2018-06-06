# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list 
# that are less than 5.

lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
minor_five = []

for num in lista:
    if num < 5:
        print(num)

# Instead of printing the elements one by one, 
# make a new list that has all the elements less than 5 from this list in it 
# and print out this new list.

for num in lista:
    if num < 5:
        minor_five.append(num)
print(minor_five)

# Ask the user for a number and return a list 
# that contains only elements from the original list 
# a that are smaller than that number given by the user.

pedido = int(input("Digite um número inteiro: \n"))

minor_pedido = []
for num in lista:
    if num < pedido:
        minor_pedido.append(num)
print(minor_pedido)

