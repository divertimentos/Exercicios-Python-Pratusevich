'''
 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
'''

lines = " ---"  # Traços
pipes = "|   "  # Pipes esquerdo e direito
boardline = [lines, pipes]

size = 3

for i in range(1):
    for j in boardline:
           print(j * size)
print(lines * size)