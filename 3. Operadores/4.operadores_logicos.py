# Combinar condiciones.
edad = 18
tiene_licencia = True

# and. Si ambas son verdaderas es True.
edad >= 18 and tiene_licencia

# or. Si alguna es verdadera es True.
edad <= 18 or tiene_licencia

# not
not edad >= 18


# Pedir la edad del usuario y verificar si esta entre 18 y 30 años. Mostrar un mensaje si está en el rango o no.

edad_usuario = int(input("ingresa tu edad: "))
verificacion = edad_usuario >=18 and edad_usuario <=30
print(verificacion)



if verificacion:
    print("Estas medio joven")

elif not verificacion:
    print("Tampoco me sirves")

else: 
    print("no me sirves chaval")