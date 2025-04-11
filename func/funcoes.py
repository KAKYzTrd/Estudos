def clear(n,n1):
  from rich.console import Console
  from time import sleep
  
  sleep(n)
  Console().clear()
  sleep(n1)

def int_input (prompt):
  while True:
    try:
      return int (input(prompt))
    except ValueError:
      clear(0,0)
      print('Por favor digite um número')
      clear(2,0)

def float_input (prompt):
  while True:
    try:
      return float (input(prompt))
    
    except ValueError:
      clear(0,0)
      print('Por favor digite um número')
      clear(2,0)

def str_input (prompt):
  return str (input(prompt))