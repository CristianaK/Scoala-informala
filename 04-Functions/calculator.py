#2 var
#1operator
#1 rezulat

def suma(a: int,b: int) -> str:
    return f"{a} + {b} = {a+b}"

def diferenta(a: int, b: int) -> str:
    return f"{a} - {b} = {a - b}"

def inmultire(a: int, b: int) -> str:
    return f"{a} * {b} = {a * b}"

def impartire(a: int, b: int) -> str:
    if b == 0:
        while b == 0:
                 b = input("Aloca o noua valoarea pentru b: ")
    return f"{a} / {b} = {a/b}"

def operator() -> str:
    op = input("Alege operatorul: ")
    if op in ['*', '/', '-', '+']:
        while op not in ['*', '/', '-', '+']:
            op = input("Alege operatorul: ")
    return op

def conversie(mesaj_input: str):
    nr = input(f"{mesaj_input}")
        while nr.isdigit() is False:
            nr = input(f"{mesaj_input}")
    return int(nr)

def calculator() -> str:
#  nr1 = input("Prmul numar: ")
 # if nr1.isdigit:
 #    nr1 = int(nr1)
 # else:
 #    while nr1.isdigit() is False:
#       nr1 = input("Primul numar: ")

#  nr2 = input("Al doilea numar:")
# if nr2.isdigit:
 #    nr2= int(nr1)
#  else:
     #   while nr2.isdigit() is False:
     #       nr2 = input("Al doilea numar: ")

    nr1 = conversie("Primul numar: ")
    nr2 = conversie("Al doilea numar:")
    op = operator()
    if op == '+':
        rezultat = suma(nr1, nr2)
    elif op == '-':
        rezultat = diferenta(nr1, nr2)
    elif op == '*':
        rezultat = inmultire(nr1,nr2)
    elif op == '/':
        rezultat = impartire(nr1, nr2)
    return rezultat

print(calculator())