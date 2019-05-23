import sys

def asciiArr(st):
  re = []
  for c in st:
    re.append(ord(c))
  return re

def asciiVal(st):
  re = "";
  for c in st:
    re += str(ord(c))
  return int(re)

def asciiSum(intArr):
  re = 0
  for i in intArr:
    re += i
  return re

def getSum(num):
  st = str(num)
  re = 0
  while len(st) > 1:
    re = 0
    for i in st:
      re += int(i)
    st = str(re)
  return re

if len(sys.argv)>1:
  # Option 1:
  #a = asciiArr(sys.argv[1]) #
  #b = asciiSum(a)           #
  #c = getSum(b)             #
  #print(str(c))             #
  #--------------------------#
  # Option 2:                #
  a = asciiVal(sys.argv[1])
  b = getSum(a)
  print(str(b))