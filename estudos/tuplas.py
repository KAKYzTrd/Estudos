import sys
sys.path.insert(0, '/sdcard/Estudos/func')
from funcoes import *
from time import sleep as wait

def extenso ():
  num = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
  nome = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
  
  while True:
    clear(0,0)
    n = int_input('Digite um número entre 0 e 20:\n > ')

    if n < 0 or n > 20:
      clear(0,0)
      print('Por favor digite um número entre 0 e 20')
      clear(3,0)
      continue
    else:
      exten = num.index(n)
      print(f'\nVoce digitou o numero {nome[exten]}')

    wait(4)
    clear(0,0)

    while True:
      ask = str_input('Deseja continuar? [S/N]\n > ')

      if ask not in 'SsNn':
        clear(0,0)
        print('Por favor digite S para sim ou N para não')
        clear(3,0)

      else:
        clear(0,0)
        break
    
    if ask in 'Ss':
      continue
    else:
      print('Encerrando')
      wait(3)
      return

extenso ()