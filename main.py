#.\venv\Scripts\python.exe -m pip install matplotlib
#.\venv\Scripts\python.exe -m pip install networkx
#import matplotlib.pyplot as plt
#import networkx as nx

from Repl import *
from ASM import ASM
from Util import Util
from Consts import Consts

def prompt():
  ASM.newFile()
  ASM.setStart("_start")
  Repl().cmdloop()
  ASM.setReturnDefault(1)
  for s in ASM.stack:
    Util.writeFileAppend(Consts.ASM, s)
    print(s, end='')

def test(w):
  Repl().analisador(w)

if __name__ == "__main__":
  #test("let n1 = 1+2*(4+5)") # 19
  #test("let n2 = 10") # 10
  #test("n1*n2^2") # 1900
  #test("n1+2*n2") # 39
  #test("2+a")
  #test("let a = 2")
  #test("3+a")
  
  #test("l1 = [1, 2, 3, 4] ")
  #test("l2 = [2, 3] ")
  #test("g = @")
  #test("g + l1")
  #test("g - l2")
  prompt()
  
  """
  g = Graph()
  g.addEdges(1, [2,3, 4])
  g.addEdges(2, [3])
  print(g)
  print(f"Remove vEdge: {g.popEdge(2,3)}")
  print(f"Remove vEdge: {g.popEdge(1,2)}")
  print(f"Remove vEdge: {g.popEdge(1,4)}")
  print(g)
  print(f"Remove vertice 1: {g.popV(1)}")
  print(f"Remove vertice 2: {g.popV(2)}")
  print(f"Remove vertice 3: {g.popV(3)}")
  print(f"Remove vertice 4: {g.popV(4)}")

  """
