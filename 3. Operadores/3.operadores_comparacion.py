# Operadores de comparación. Comparan valores y devuelven True o False.
n1 = 3
n2 = 5
n3 = 3


# Igual que
n1 == n3

# Diferente 
n1 != n2

# Mayor que
n1 > n2

# Menor que
n2 < n3

# Mayor o igual
n1 >= n2

# Menor o igual
n2 <= n3


# Pedir la edad al usuario y mostrar si es mayor o igual a 18
edad_usuario = int(input("ingrese su edad: "))
tof = edad_usuario >= 18
print(tof)

# Comparar si dos palabras ingresadas por el usuario son iguales.
palabra_1 = input("ingresa tu palabra 1: ")
palabra_2 = input("ingresa tu palabra 2: ")
comparacion = palabra_1 == palabra_2    

print(comparacion)