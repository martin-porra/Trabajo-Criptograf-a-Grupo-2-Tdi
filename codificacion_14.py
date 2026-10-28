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

# --- Datos del Ejercicio 14 ---
n = 536813567
e = 3602561

# Paso 1: Obtener p y q
p, q = fermat(n)

# Paso 2: Calcular phi(n)
phi_n = (p - 1) * (q - 1)

# Paso 3: Calcular la clave privada d

d = pow(e, -1, phi_n)

print(f"1. Factores primos: p = {p}, q = {q}")
print(f"2. Indicador de Euler phi(n) = {phi_n}")
print(f"3. Clave privada d = {d}")
print(f"\n-> Par de clave privada para descifrar: (n, d) = ({n}, {d})")
