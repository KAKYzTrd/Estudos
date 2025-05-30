import sys
sys.path.insert(0, '/sdcard/Estudos/python/func')
from funcoes import *
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
