'''def get_integer():
    n = int(input("Give me a number: \n"))
    return print(n * 2)  # teste: retornar o dobro da entrada
get_integer()
'''

def get_integer(help_text):
    return int(input(help_text))

age = get_integer("Sua idade: \n")
schoolyear = get_integer("Em que ano você estuda: \n")

if age > 15:
    print("Você tem mais de 15 anos.")
print(f"Você está no {schoolyear}º ano.")
