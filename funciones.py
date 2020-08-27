def enumeracion (objetivo):
  respuesta =0
  while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1
  
  if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
  else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')

def aproximacion (objetivo):
  import time
  from time import gmtime, strftime
  epsilon = 0.0001
  #Que tanto nos vamos a ir acercando en cada iteracion a la respuesta.
  paso= epsilon**2

  respuesta = 0.0

  start_time = time.time()
  print(strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + ' >>> Iniciando...')

  #la primera condicion nos indica que nos estamos acercando al objetivo
  #mientras que la segunda nos protege contra numeros negativos.
  while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2-objetivo), respuesta)
    #En cada Iteracion le sumamos el paso a la respuesta
    respuesta += paso
  
  if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raiz cuadrada de {objetivo}')
  else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

  end_time = time.time()
  hours, rem = divmod(end_time - start_time,3600)
  minutes, seconds = divmod(rem,60)
  print(strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + " TOTAL TIME: {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))


def busqueda_binaria (objetivo):
  epsilon = 0.0015891
  bajo = 0.0
  alto = max(1.0, objetivo)
  respuesta = (alto + bajo) / 2
  
  while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo = {bajo}, alto = {alto}, epsilon = {epsilon}, respuesta = {respuesta}')
    if respuesta**2 < objetivo:
      bajo = respuesta
    else:
      alto = respuesta
  
    respuesta = (alto + bajo) / 2
  
  print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def run():
  opcion = int(input('''
    Selecciona el Algoritmo que deseas usar:
    1. Enumeracion.
    2. Aproximación.
    3. Búsqueda Binaria 
    4. Salir'''))
      
  while opcion != 4:
        
    objetivo = int(input('Escoge un entero: '))
    
    if opcion == 1:
      enumeracion(objetivo)
    elif opcion ==2:
      aproximacion(objetivo)
    elif opcion == 3:
      busqueda_binaria(objetivo)
    elif opcion == 4:
      print('Adios!')
    else: 
      print('Opcion incorrecta!')
    
    opcion = int(input('''
    Selecciona el Algoritmo que deseas usar:
    1. Enumeracion.
    2. Aproximación.
    3. Búsqueda Binaria 
    4. Salir'''))

if __name__ =="__main__":
  run()