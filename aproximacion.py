objetivo = int(input('Dame un numero objetivo: '))
#¿Que tan cerca queremos llegar de la respuesta
epsilon = 0.01
#Que tanto nos vamos a ir acercando en cada iteracion a la respuesta.
paso= epsilon**2

respuesta = 0.0
#la primera condicion nos indica que nos estamos hacercando al objetivo
#mientras que la segunda nos protege contra numeros negativos.
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
  #En cada Iteracion le sumamos el paso a la respuesta
  respuesta += paso
  
if abs(respuesta**2 - objetivo) >= epsilon:
  print(f'No se encontró la raiz cuadrada de {objetivo}')
else:
  print(f'La raiz cuadrada de {objetivo} es {respuesta}')