def P(a, b):
    return a + b

def M(a, b):
    return a - b

def U(a, b):
    return a * b

def D(a, b):
    return a / b

a = int(input())
b = int(input())
c = str(input())

if c == '+':
  print(P(a, b))

if c == '-':
  print(M(a, b))

if c == '/':
  print(D(a, b))

if c == '*':
  print(U(a, b))