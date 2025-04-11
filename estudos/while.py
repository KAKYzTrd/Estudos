import sys
sys.path.insert(0, '/sdcard/peiton/func')
from funcoes import *
from math import factorial
from random import randint

def sex ():
  sexo = str_input("Qual e o seu sexo [F/M]\n > ").upper().strip()
  
  while sexo not in "FfMm":
    limpar(0,0)

    sexo = str_input("Qual e o seu sexo [F/M]\n > ").upper().strip()

  print(f'Sexo {sexo} registrado com sucesso')

def adivinha ():
  n_secreto = randint(0,10)
  i = 1
  receba = True
  print('Seja bem vindo ao game')
  clear(3,0)
  print('Estou pensando em um numero tente adivinhar qual é')
  clear(3,0)
  
  while receba:
    n = int_input(f'Tentativa N°{i}\n > ')
    i += 1

    if n_secreto == n :
      clear(0,0)
      print(f'Parabens voce venceu!!!!\ncom {i} tentativas')
      receba = False

    elif n_secreto < n:
      print('\nTente um número menor')
      clear(2,0)

    elif n_secreto > n:
      print('\nTente um número maior')
      clear(2,0)

def menu ():
  n = int_input('Digite o primeiro valor:\n > ')
  n1 = int_input('\nDigite o segundo valor:\n > ')
  while True:
    clear(0,0)
    print(
'''
| 1 | Somar
| 2 | Multiplicar
| 3 | Maior
| 4 | Novos números
| 5 | Sair
'''
      )
    opcao = str_input('Selecione a opcao desejada:\n > ')

    if opcao == '1':
      print(f'\nA soma entre {n} + {n1} = {n + n1}')
      clear(4,0)

    elif opcao == '2':
      print(f'\nA Multiplicação entre {n} • {n1} = {n * n1}')
      clear(4,0)

    elif opcao == '3':
      print(f'\nO maior entre {n} e {n1} é {max(n1,n)}')
      clear(4,0)

    elif opcao == '4':
      clear(0,0)
      n = int_input('Digite o primeiro valor:\n > ')
      n1 = int_input('\nDigite o segundo valor:\n > ')
      clear(0,0)
      continue

    elif opcao == '5':
      clear(0,0)
      break

    else:
      clear(0,0)
      print('Opção inválida')
      clear(2,0)

def fatorial ():
  n = int_input('Digite um numero:\n > ')
  f = factorial(n)
  clear(0,0)
  print(f'{n}! e igual á:\n\n', end=(''))
  while n > 0:
    print(f'{n}', end=(''))
    print(' • ' if n > 1 else ' = ', end=(''))
    n -= 1
  
  print(f' {f}')
  
def pa ():
  print('Gerador de PA')
  cont = 1
  pause = 11

  clear(3,0)
  termo = int_input('Digite o primeito termo:\n > ')
  razao = int_input('\nDigite a razão:\n > ')
  clear(0,0)
  
  while cont < pause:
    print(f'{termo} -> ', end=(''))
    termo += razao
    cont += 1
    
    if cont == pause:
      print('Pausa')
      n = int_input('\nQuantos termos deseja adicionar:\n > ')
      print()
      pause += n

      if n == 0:
        break
  
  print(f'\nprograma encerrado com {cont} termos apresentados')

def fibonacci ():
  t1 = 0
  t2 = 1
  cont = 3
  print('Sequencia de Fibonacci')
  
  clear(3,0)
  n = int_input('Quantos termos voce deseja ver:\n > ')
  print(f'{t1} -> {t2}', end='')
  while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3} ', end='')
    t1 = t2
    t2 = t3
    cont += 1
  print('Fim')

def numeros ():
  cont = 0
  soma = 0

  n = int_input('Digite um número [ 999 para sair]:\n > ')
  clear(0,0)

  while n != 999:
    clear(0,0)
    soma += n
    cont += 1
    n = int_input('Digite um número [ 999 para sair]:\n > ')

  print(f'Voce digitou {cont} números a soma entre eles é {soma}')

def maioremenor ():
  contador= 0
  condicao = 'S'
  lista = []
  
  while condicao in 'S':

    n = int_input('Digite um número:\n > ')
    clear(0,0)
    contador += 1
    lista.append(n)


    condicao = str_input('Deseja continuar? [S/N]\n > ').upper()
    clear(0,0)
  
  print(f'Voce digitou {contador} números e a média foi {sum(lista) / len(lista):.2f}\nO maior número digitado foi {max(lista)} e o menor foi {min(lista)}')

def tabuada ():
  while True:
    n = int_input('Digite um número:\n > ')
    clear(0,0)

    for i in range(1,11):
      print(f'{n}x{i} = {i * n}')
    
    clear(3,0)

def parouimpar ():
  print('Vamos jogar Par ou Impar')
  clear(3,0)
  v = d = 0
  while True:
    n_computador = randint (0,11)

    n = int_input('Digite um valor de 0 a 10:\n > ')
    if n > 10:
      clear(0,0)
      print('Por favor digite um numero entre 0 e 10')
      clear(3,10)
 
    soma = n_computador + n
    clear(0,0)

    while True:
      escolha = str_input('Par ou Impa [P/I]:\n > ').upper().strip()
      if escolha not in 'PI':
        clear(0,0)
        print('Valor invalido')
        clear(3,0)
      else:
        break
 

    if soma % 2 == 0 and escolha == 'P':
      print(f'seu número foi {n}\n e o meu foi {n_computador}\n o resultada soma entre eles foi {soma}')
      clear(4,0)
      print('Voce venceu!!')
      v += 1

    elif soma % 2 != 0 and escolha == 'I':
      print(f'seu número foi {n}\n e o meu foi {n_computador}\n o resultada soma entre eles foi {soma}')
      clear(4,0)
      print('Voce venceu!!')
      v += 1

    else:
      print(f'seu número foi {n}\n e o meu foi {n_computador}\n o resultada soma entre eles foi {soma}')
      clear(4,0)
      print('Que pena campeão não foi desta vez T-T')
      d += 1
 
    clear(3,0)

    while True:
      jogar_denovo = str_input('Deseja jogar novamente? [S/N]\n > ').upper().strip()

      clear(0,0)

      if jogar_denovo == 'S':
        break
  
      elif jogar_denovo == 'N':
        print('Foi legal jogar contra voce')
        clear(3,0)
        print(f'Placar:\n\nVitorias : {v}\nDerrotas: {d}\n\n')
        print('Droga voce venceu ^^' if v > d else 'Bem eu acabei perdendo T-T')
        return
  
      else:
        print('Resposta inválida')
        clear(3,0)

def cadastro ():
  mais18 = homem = mulher = 0

  while True:
    print('-'*20)
    print('     CADASTRE-SE')
    print('-'*20)

    idd = int_input('Idade: ')
    if idd > 18:
      mais18 += 1

    while True:
      sexo = str_input('Sexo [M/F] : ').upper().strip()
      
      if sexo not in 'MF':
        clear(0,0)
        print('Sexo inválido')
        clear(3,0)
      else:
        clear(0,0)
        break
  
    if idd < 20 and sexo == 'F':
      mulher += 1
    elif sexo == 'M':
      homem += 1
    
    while True:
      continuar = str_input('Deseja cadastrar outra pessoa? [S/N]\n > ').upper().strip()
      if continuar not in 'SN':
        clear(0,0)
        print('Opção inválida')
        clear(3,0)
      else:
        clear(0,0)
        break

    if continuar == 'S':
      continue
    else:
      print('Encerrando')
      sleep(3)
      break

  print(
f'''
Total de pessoas com mais de 18 anos: {mais18}
Ao todo temos {homem} homens cadastrados
E temos {mulher} mulher com menos de 20
''')

fatorial ()