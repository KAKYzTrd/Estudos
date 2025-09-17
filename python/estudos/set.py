import os
os.system('cls || clear')

def sets ():

    s1 = set() # <-- VAZIO
    s2 = [1, 2, 2, 3, 3 ,3 ]
    print(3 in set(s2))

def add ():
    s1 = set()
    s1.add('Luiz')
    s1.add('Marcelo')
    s1.update('Faz o L')
    print(s1)

def Operadores ():
    #União | (union) - line 
    #Intersecção & (intersection) - itens presentes em ambos
    #diferença - itens presentes apenas no set da esquerda
    #diferença simetrica ^ - itens que não estão em ambos
    s1 = {1, 2, 3}
    s2 = {4, 5, 6, 3}
    s3 = s1 | s2
    s3 = s1 & s2
    s3 = s1 - s2
    s3 = s1 ^ s2

    print(s3)

Operadores()