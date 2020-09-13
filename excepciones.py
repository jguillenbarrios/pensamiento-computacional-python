
def divide_elementos_de_lista(lista, divisor):
    #list comprehension
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as  e:
        '''El programa no truena, si esta excepcion sucede, simplemente regresa la lista'''
        print(e)
        return lista


lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))