#bloc organizat de cod ce poate fi refolosit

#print("afisare mesaj")
#format(string)
#a = input("de la tastatura")

#def functia_mea(param_1):
 #   pass

def suma(a: int, b: int =1, c: int=3) -> (int, int):
    """"
    :param a: first param
    :param b: second param
    :param c: third param
    :return: sum o f params, dif of params
    """
    return a+b+c, a-b-c

variabila_1 = 1
variabila_2 = 2

sum, dif = suma(a=variabila_1, b=variabila_2, c= 0)
print(sum, dif)
