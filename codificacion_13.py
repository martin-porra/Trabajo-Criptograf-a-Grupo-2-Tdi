import math 
def fermat(n):
 if n % 2  == 0:
  return 2,n // 2
 x = math.ceil(math.sqrt(n))
 print(f"Primer entero mayor o igual a la raiz cuadrada de n: {x}")
 while True:
   y_cuadrado = x * x - n
   y = int(math.isqrt(y_cuadrado))
   print(f"Con x = {x}: {x} x {x} - {n} = {y_cuadrado}")
   yy = y * y
   if yy == y_cuadrado:
        print(f' y = {y_cuadrado} es un cuadrado perfecto')
        p = x + y
        q = x - y
        return p, q
   else:
     print(f' y={y_cuadrado} no es cuadrado')
   x += 1   
n = 2291
p, q = fermat(n)
print(f"Los factores primos de {n} son: p = {p}, q = {q}")