import random

lista = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]


def valoare_utilizator():
    while True:
        pozitie = int(input("Alege o pozitie goala  de la 1 la 9"))
        if pozitie > 0 and pozitie < 10:
            if lista[pozitie - 1] == "_":
                return lista[pozitie - 1] = '[X]'
            else:
                print("Pozitia este deja ocupata!")

print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{}" .format(lista[0], lista[1], lista[2], lista[3], lista[4],lista[5], lista[6], lista[7], lista[8]))


while "_" in lista:

    if lista[4] == "_":
        lista[4] = '[0]'
    elif lista[0] == "_":
        lista[0] = '[0]'
    elif lista[2] == "_":
        lista[2] = '[0]'
    elif lista[6] == "_":
        lista[6] = '[0]'
    elif lista[8] == "_":
        lista[8] = '[0]'
    else:
        ramas = [1, 3, 5, 7]
        computer_choice = random.choice(ramas)
        while computer_choice not in ramas:
            lista[computer_choice] = '[0]'
            break




def castigator():


    if lista[0] == lista [1] == lista[2] == '[X]':
        x_castigator = True

    elif lista[3] == lista[4] == lista [5]  == '[X]':
        x_castigator = True
    elif lista[6] == lista[7] == lista[8]  == '[X]':
        x_castigator = True
    elif lista[0] == lista[3] == lista[6]  == '[X]':
        x_castigator = True
    elif lista[1] == lista[4] == lista[7]  == '[X]':
        x_castigator = True
    elif lista[2] == lista[5] == lista[8]  == '[X]':
        x_castigator = True
    elif lista[0] == lista[4] == lista[8]  == '[X]':
        x_castigator = True
    elif lista[2] == lista[4] == lista[6]  == '[X]':
        x_castigator = True
    return print('Ai castigat!')

def loser():
    if lista[0] == lista [1] == lista[2] == '[0]':
        x_castigator = False

    elif lista[3] == lista[4] == lista [5]  == '[0]':
        x_castigator =  False
    elif lista[6] == lista[7] == lista[8]  == '[0]':
        x_castigator =  False
    elif lista[0] == lista[3] == lista[6]  == '[0]':
        x_castigator =  False
    elif lista[1] == lista[4] == lista[7]  == '[0]':
        x_castigator = False
    elif lista[2] == lista[5] == lista[8]  == '[0]':
        x_castigator = False
    elif lista[0] == lista[4] == lista[8]  == '[0]':
        x_castigator = False
    elif lista[2] == lista[4] == lista[6]  == '[0]':
        x_castigator = False
    return print('Ai pierdut!')