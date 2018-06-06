# Create a program that asks the user for a number 
# and then prints out a list of all the divisors of that number.

# (If you don’t know what a divisor is, 
# it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Digite um número: \n"))

lista_numeros = list(range(1, num + 1))
lista_divisores = []

for i in lista_numeros:
    if num % i == 0:
        lista_divisores.append(i)
print(lista_divisores)
