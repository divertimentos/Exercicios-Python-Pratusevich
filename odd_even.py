# Ask the user for a number. 
# Depending on whether the number is even or odd, 
# print out an appropriate message to the user.

# Hint: how does an even / odd number react differently when divided by 2?

num = int(input("Digite um número: \n"))

if num % 2 == 0:
    print("O número %d é par." % (num))
    # If the number is a multiple of 4, print out a different message:
    if num % 4 != 0:
        print(f"O número {num} não é múltiplo 4")
    else:
        print("O número %d é múltiplo de 4." % (num))
else:
    print("O número %d é ímpar." % (num))

# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. 
# If not, print a different appropriate message.

num = int(input("Digite outro número: \n"))
divide = int(input("Digite um divisor: \n"))

if num % divide == 0:
    print("O número %d é divisível por %d!" % (num, divide))
else:
    print("O número %d não é um divisor inteiro de %d!" % (num, divide))
