# Litte Perfomance test
# finds names from csv, matching to given checksum 
# python3 processNames.py longlist.csv 9

import sys
from colorama import Fore, Back, Style

def asciiVal(st):
  re = "";
  for c in st:
    re += str(ord(c))
  return int(re)

def getSum(num):
  st = str(num)
  re = 0
  while len(st) > 1:
    re = 0
    for i in st:
      re += int(i)
    st = str(re)
  return re

def getFileContent(p):
  f = open(p,"r")
  return f.read()

def getLines(st):
  return st.split("\n")

def getValues(ln):
  return ln.split(";")

def processfile(f,target):
  lns = getLines(f)
  hits = []
  for ln in lns:
    if ln != "":
      vals = getValues(ln)
      if vals[1] != "" and vals[2] == "m":
        a = asciiVal(vals[1])
        b = getSum(a)
        if b == target:
          print(Fore.GREEN + vals[1])
          hits.append(vals[1])
        else:
          print(Fore.WHITE + vals[1])
  return hits

def printNames(names):
  for n in names:
    print(Fore.YELLOW + n)

if len(sys.argv) > 2:
  f = getFileContent(sys.argv[1])
  re = processfile(f,int(sys.argv[2]))
  print(Fore.GREEN + str(len(re))+"/"+str(len(getLines(f))))
  #printNames(re)
