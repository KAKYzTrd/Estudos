from dataclasses import dataclass
import sys
sys.path.insert(0, "/sdcard/Estudos/python/func")
from funcoes import *
from dataclasses import dataclass
from time import sleep as wait
clear(0,0)

def imprimir ():

  nome = str_input('Digite o seu nome:\n > ')
  clear(0,0)

  idade = int_input('Digite a sua idade:\n > ')
  clear(1,2)

  print(f'Olá {nome}, voce tem {idade} e eu espero que voce se mate :\n > :\n > ')

def tipos ():

  nome = "Clarencio"
  idade = 19
  altura = 1.80
  e_gay = True

def opmatematica (n1, n2):
  
  soma = n1 + n2
  sub = n1 - n2
  mult = n1 * n2
  div = n1 // n2
  
  print(
f'''
Operções Matematicas
  
Soma: {soma}
Subtração: {sub}
Multiplicação: {mult}
Divisão: {div}
'''
        )

def condicao ():
  
  idade = int_input('Quantos anos voce tem?:\n > ')
  clear(0,2)
  
  if idade >= 18:
    print('Voce esta apto a dirigir')

  else:
    print('Voce e menor de idade T-t')

def contagem ():
  n = 10
  pinto = 0
  while pinto != n:

    print(pinto)
    pinto += 1
  
def maior (n1,n2):
  if n1 > n2:
    print(f'{n1} é maior que {n2}')

  else:
    print(f'{n2} é maior que {n1}')

def lista ():
  num = []

  for i in range(5):
    n = int_input(f' Digite o {i + 1}° numero:\n > ')
    clear(0,0)

    num.append(n)
  
  print(f'O maior numero digitado e {max(num)}\nE o menor numero digitado é {min(num)}')

def aluno ():

  Aluno = {
    "Nome": "Andre",
    "Idade": 17,
    "Notas": [10,7]
  }

  print(
f'''
Aluno: {Aluno["Nome"]}
Idade: {Aluno["Idade"]}
Notas totais : {sum(Aluno["Notas"])}
Media final: {sum(Aluno["Notas"]) / 2}
'''
        )

def vogal ():

  n = "minha pika ta muito dura"
  vogais = 0
  for letra in n:
    if letra in 'aeiou':
      vogais += 1
  
  print(
f'''
Na frase: {n}
há: {vogais} vogais
'''
        )

def maior ():

  @dataclass
  class Pessoa:
    nome : str
    idade : int
  
    def maioridade(self):
      return self.idade >= 18

  nome = str_input('Digite o seu nome:\n > ')
  clear(0,0)
  
  idade = int_input('Digite a sua idade:\n > ')
  clear(0,0)

  pessoa = Pessoa(nome, idade)

  if pessoa.maioridade():
    print(f'Olá {pessoa.nome} voce é maior de idade')

  else:
    print(f'Olá {pessoa.nome} voce é menor de idade')

def salvar ():
  nome = "Pika dura"
  
  with open('Xereka', 'w') as arquivo:
    arquivo.write(f'{nome}')

def random():
  from random import randint
  n = randint(0,10)
  tent = 1
  ns = 0

  while n != ns:
    ns =  int_input(f'Digite o {tent}° numero:\n > ')
    clear(0,0)
    tent += 1
  
  print(f'Voce ganhou com {tent - 1 } tetativas')
