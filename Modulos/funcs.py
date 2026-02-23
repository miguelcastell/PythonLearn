def somar():
    print('Esta função irá somar dois números')

def multiplicar():
    print('Esta função irá multiplicar dois números')

def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1