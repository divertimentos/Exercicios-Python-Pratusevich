# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

word = str(input("Descubra se uma palavra é um palíndromo: \n")).lower()

if word == word[::-1]:
    print(f"A palavra {word} é um palíndromo.")
else:
    print(f"A palavra {word} não é um palíndromo.")
