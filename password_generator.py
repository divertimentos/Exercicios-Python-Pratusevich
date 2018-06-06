import random

'''
Write a password generator in Python. 
Be creative with how you generate passwords 
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password 
every time the user asks for a new password. 
Include your run-time code in a main method.
'''
# O seguinte código não é meu, é da Pratusevich:

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = int(input("Tamanho da senha: \n"))
p  = "".join(random.sample(s, passlen))
print(p)
