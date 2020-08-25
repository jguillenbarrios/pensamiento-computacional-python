import time
from time import gmtime, strftime

objetivo = int(input('Dame un numero objetivo: '))
#¿Que tan cerca queremos llegar de la respuesta
epsilon = 0.0001
#Que tanto nos vamos a ir acercando en cada iteracion a la respuesta.
paso= epsilon**2

respuesta = 0.0

start_time = time.time()
print(strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + ' >>> Iniciando...')

#la primera condicion nos indica que nos estamos hacercando al objetivo
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