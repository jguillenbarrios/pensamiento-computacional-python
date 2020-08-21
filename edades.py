nombre_1= input('Escribe tu nombre: ')
num_1 = int(input('Escribe tu edad: '))

nombre_2= input('Dame el segundo nombre: ')
num_2 = int(input('Dame la otra edad: '))

if num_1 > num_2:
  print(f'{nombre_1} es mayor que {nombre_2}')
elif num_1 < num_2:
  print(f'{nombre_2} es mayor que {nombre_1}')
else:
  print(f'{nombre_1} y {nombre_2} tienen la misma edad!')