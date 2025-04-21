import sys
sys.path.insert(0,'/sdcard/Estudos/python/funcc')
from funcoes import *
from time import sleep as wait


def produtos ():
  Pratos = [
    {"ID": 1, "Qtd": 0, "Nome": "Picanha", "Preço": 25.00},
    {"ID": 2, "Qtd": 0, "Nome": "Lasanha", "Preço": 20.00},
    {"ID": 3, "Qtd": 0, "Nome": "Estrogonoff", "Preço": 18.00},
    {"ID": 4, "Qtd": 0, "Nome": "Feijoada", "Preço": 15.00},
    {"ID": 5, "Qtd": 0, "Nome": "Pure de batata", "Preço": 10.00}
    ]
  return Pratos

def menu ():
  clear(0,0)
  print(
'''
============ Menu ==============
| 1 | Picanha           R$25,00|
| 2 | Lasanha           R$20,00|
| 3 | Estrogonoff       R$18,00|
| 4 | Feijoada          R$15,00|
| 5 | Pure de batata    R$10,00|
================================
| 0 | Sair                     |
================================
'''
    )

def continuar ():
  while True:
    continuar = str_input('Deseja continuar? [S/N]\n > ').upper()

    if continuar not in ['S', 'N']:
      clear(0,0)
      print('Por favor digite S para sim e N para não')
      clear(2,0)
  
    else:
      break
  
  return continuar

def programa ():
  vl = 0
  Produtos = produtos()
  compras = []
  
  while True:
    menu ()
    
    Id = int_input('Digite o ID desejado:\n > ')
    
    for compra in compras:
      if compra["ID"] == Id:
        compra["Qtd"] += 1
        clear(0,0)
        print(f'{compra["Nome"]} adicionado com sucesso!!')
        clear(2,0)
        break

    else:
      for prato in Produtos:
        if prato["ID"] == Id:
          prato["Qtd"] += 1
          compras.append(prato)
          clear(0,0)
          print(f'{prato["Nome"]} adicionado com sucesso')
          clear(2,0)
          break

      else:
        print('Prato não encontrado')

    outro_id = continuar ()
    if outro_id in 'S':
      continue

    else:
      break

  for item in compras:
    Valor = item["Preço"] * item["Qtd"]
    vl += Valor
    print(
f'''
======= {item["ID"]} =======
Nome: {item["Nome"]}
Quantidade: {item["Qtd"]}
valor: R${item["Qtd"] * item["Preço"]:.2f}
'''
      )
  
  print(f'\nO valor total a se pagar é de: R${vl:.2f} ')

def main ():
  programa ()

if __name__ == "__main__":
  main()