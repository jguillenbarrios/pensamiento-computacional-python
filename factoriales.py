def factorial(n):
  """Calcula el factorial de n
  Args:
      n (int): cualquien entero mayor de 0
  """
  print(n)
  if n == 1:
    return 1
  
  return n * factorial(n-1)

n = int(input('Escribe un entero: '))
print(factorial(n))
