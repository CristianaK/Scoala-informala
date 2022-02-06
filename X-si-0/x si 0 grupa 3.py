import random
intrebare = input("Vrei sa incepi jocul? 'y/n'")

lista = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

if intrebare == 'y':
    valoare_utilizator = int(input("Alege un numa de la 1 la 9"))
    if lista[valoare_utilizator - 1] == "_":
        lista[valoare_utilizator - 1] = '[X]'

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

    print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{}" .format(lista[0], lista[1], lista[2], lista[3], lista[4],lista[5], lista[6], lista[7], lista[8]))

    valoare_utilizator = int(input("Alege un numa de la 1 la 9"))
    if lista[valoare_utilizator - 1] == "_":
        lista[valoare_utilizator - 1] = '[x]'

    if lista[0] == lista [1] == lista[2] != "_":
        if lista[0] == '[x]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[3] == lista[4] == lista [5] != "_":
        if lista[3] == '[X]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[6] == lista[7] == lista[8] != "_":
        if lista[6] == '[X]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[0] == lista[3] == lista[6] != "_":
        if lista[0] == '[x]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[1] == lista[4] == lista[7] != "_":
        if lista[1] == '[x]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[2] == lista[5] == lista[8] != "_":
        if lista[2] == '[x]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[0] == lista[4] == lista[8] != "_":
        if lista[2] == '[x]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[2] == lista[4] == lista[6] != "_":
        print(f'Ai castigat!, {lista[2]}')


