producto = "Manzana"
precio = 1500
disponible = True


# Tipos de datos.
string = "Cadena de Texto" 
int = 21313 # Numero Enteros
float = 3.14 # Numeros decimales


# Verificación de tipos de datos.
print(type(string))


# Las variables en Python son reasignables.
string = "Numero"


# Reasignacion multiple
a, b, c = 1, 2, 3


# Conversión de tipos (Casting)

# Entero a texto
edad = 20
texto = str(edad)

# Texto a entero
numero = int("25")

# Texto a decimal
decimal = float("3.14")


# f-string. Permite añadir variables a los print sin necesidad de añadir operadores de concatenación.
print(f"Mi edad es: {edad}")


# Mini Ejercicios
"""
    1. Crea una variable con tu nombre y otra con tu edad, luego imprímelas.
    2. Declara tres variables con tu comida, color y número favorito en una sola línea.
    3. Convierte el número 5 a texto y verifica el tipo con type().
    4. Muestra un mensaje personalizado, que incluya el nombre, la edad y ciudad.
    6. 
"""