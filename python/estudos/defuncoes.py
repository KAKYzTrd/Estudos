def clear(n,n1):
  from rich.console import Console
  from time import sleep 
  
  sleep(n)
  Console().clear()
  sleep(n1)

clear(0,0)

def nomeado():
  def soma(x=None, y=None):
    
    if x and y is not None:
      print(f' {x=} {y=} | x + y = {x + y}')
      
    else:
      print(f' x= Null y= Null | x + y = Null')
    
  soma(3, 2)
  soma(y= 2, x= 3)
  soma()

nomeado()
