import sys
sys.path.insert(0, "/sdcard/Estudos/python/func")
from funcoes import *
clear(0,0)

def save (n):
  with open("lista_metodos", "a") as arquivo:
    arquivo.write(n)

def indice ():
  #        0  1  2  3  4
  lista = [1, 2, 3, 4, 5]
  listaa = [6, 7, 8, 9, 10]
  # listab = lista + listaa ou lista.extend(listaa)
  # lista.insert(1, "Penis")
  # del lista[0]
  lista.pop()
  print(lista)

def copy ():
  lista_a = ['Sergio', 'Paola', 1, False]
  lista_b = lista_a.copy()
  
  lista_a[0] = 'Perereka'

  print(lista_a)
  print(lista_b)

def iteracao ():
  lista = ['Pedro', 'Amanda', 'josue', 'Angela', 'Emanuela']
  # n = 0

  # for nome in lista:
  #   print(n, nome)
  #   n += 1 
            # O
  for item in enumerate(lista, start= 1):
    indice, nome = item
    print(indice, nome)

def empacotamento ():
  lista = ['Pedro', 'Amanda', 'josue', 'Angela', 'Emanuela']
  nome1, *_, nome4, nome5 = lista
  
  print(*lista, sep='\n')
  print(nome1, nome4, nome5)
  print(nome1)

def tupla ():
  tupla = 'Maria', 'Jorge', 'Rogerio'
  _, nome2, *_ = tupla
  
  print(nome2)

def compra ():
  clear(0,0)
  lista = []

  while True:
    print(
'''
1 | inserir
2 | apagar
3 | listar
=============
0 | sair

'''
      )

    escolha = int_input('Selecione uma opcão:\n > ')
  
    if escolha == 1:
      clear(0,0)
  
      add = str_input('Digite o nome do produto:\n > ')
      lista.append(add)
      clear(0,0)
      continue
  
    elif escolha == 2:
      clear(0,0)
      
      if len(lista) == 0:
        print('Não há nada a ser removido')
        clear(2,0)
        continue
      
      else:
        clear(0,0)
        print('Lista de compra\n')
        for indice, nome in enumerate(lista):
          print(indice, nome)
        apagar = int_input('\nDigite o indice do item que deseja remover:\n > ')
        if apagar > (len(lista ) - 1) :
          clear(0,0)
          print('Este indice é inexistente')
          clear(2,0)
          continue
        
        else:
          clear(0,0)
          print(f"item {lista[apagar]} removido com sucesso!!")
          del lista[apagar]
          clear(2,0)
          continue
        
    elif escolha == 3:
      clear(0,0)
      if len(lista) < 1:
        print('Não ha itens na lista!!')
        clear(2,0)
        continue
      
      else:
        clear(0,0)
        print('Lista de compras\n')
        for indice, nome in enumerate(lista):
          print(indice, nome)
        wait(3)
        clear(0,0)
        continue
      
    elif escolha == 0:
      clear(0,0)
      return
    else:
      clear(0,0)
      print('opcão invalida')
      clear(2,0)
      continue

def spli ():
  '''
  strip - remove os espacos
  split - separa a frase e a transforma em uma lista
  join - separa os itens de uma lista de forma espesifica
  '''
  
  frase = 'Minha mulher, nao deixa nao'
  frase_m = frase.split()
  resul = []

  for i, frase in enumerate(frase_m):
    resul.append(frase_m[i].strip())

  uniao = '/'.join(resul)
  
  print(frase,'\n', uniao)
  
def dentro ():
  
  # Lista de lista e seus indices
  
  salas = [
     # [0][0]  [0][1]    [0][2]
    ['Maria', 'Douglas', 'Gabriel'], # 0
     # [1][0]  [1][1]
    ['Pedro', 'Roberto'], # 1
     # [2][0] [2][1]   [2][2]  [2][3]["Numeros"][5]
    ['Jose', 'Afonso', 'Ana', {"Numeros": (0, 1, 2, 3, 4, 5)}],
    ]
  #print(sala[2][3]["Numeros"][5])

  num = 0

  for sala in salas:
    num += 1
    print(f'{num}° sala')
    
    for aluno in sala:
      print(aluno)

def ternaria ():
  n = 10 
  nv = n if n == 10 else 8
  
  print('é 10' if n else 'não é 10')
  print(nv)
  print('Sim' if True else 'Não' if True else 'Fim')

def cpf ():
  cpf_num = '102487111'
  contagem = 10
  resultado = 0

  for digito in cpf_num:
   resultado += int(digito) * contagem
   contagem -= 1 
  
  valido = (resultado * 10) % 11
  
  def segundo_digito (x, y):
    cpf_num = x + str(y)
    contagem = 11
    resultado = 0
    
    for digito in cpf_num:
      mult += int(digito) * cont
      cont -= 1
    
    valido = (resultado * 10) % 11
    digito = cpf_num + str(valido)
    return valido, digito

  digito, cpf = segundo_digito(cpf_num, valido)

  if digito and seg < 10:
    print(f'O primeiro digito é: {valido}\nO segundo digito é: {digito}\n\nE este cpf é valido {cpf}')
    
  else:
    print('Seu cpf é invalido')


cpf()