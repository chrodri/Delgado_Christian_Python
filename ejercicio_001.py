Nombre = input("¿Cual es su nombre? ")
Primer_Apellido = input("¿Cual es su primer apellido? ")
Segundo_Apellido = input("¿Cual es su segundo apellido? ")
Año_Nacimiento = int(input("¿En que año naciste? "))
Dia_mes = input("¿En que mes y dia naciste? Usa formato mm-dd: ")
a,b,c,d,e = Dia_mes
Año_actual = (2023)

#Mayusculas
Nombre_Upper = Nombre.upper()
Primer_Apellido_Upper = Primer_Apellido.upper()
Segundo_Apellido_Upper = Segundo_Apellido.upper()

#Minusculas
Nombre_Lower = Nombre.lower()
Primer_Apellido_Lower = Primer_Apellido.lower()
Segundo_Apellido_Lower = Segundo_Apellido.lower()

#Edad
edad = (Año_actual-Año_Nacimiento)
edad_futura = edad+10
edad_20 = edad+20
type(edad)
media = (edad+edad_20)/2


#Nombre
Nombre_Completo = (Nombre + Primer_Apellido + Segundo_Apellido)

#Vocales
def contar_vocales(Nombre_Completo):
    contador = 0
    for letra in Nombre_Completo:
        if letra.lower() in "aeiou":
            contador += 1
    return contador

Vocales = contar_vocales(Nombre_Completo)


print(f"Tu nombre es {Nombre} {Primer_Apellido} {Segundo_Apellido}")
print(f"Este es tu nombre completo en mayusculas: {Nombre_Upper} {Primer_Apellido_Upper} {Segundo_Apellido_Upper}")
print(f"Este es tu nombre completo en minusculas: {Nombre_Lower} {Primer_Apellido_Lower} {Segundo_Apellido_Lower}")
print(f"Esta es tu fecha de nacimiento: {d}{e}-{a}{b}-{Año_Nacimiento}")
print(f"Esta es tu edad: {edad}")
print(type(edad))
print(f"Tu nombre completo tiene {len(Nombre_Completo)} letras")
print(f"Tu nombre completo tiene {Vocales} vocales")
if type(edad) == int:
    print(f"¿Tu edad es un caracter de tipo numero? {True}")
else:
    print(f"¿Tu edad es un caracter de tipo numero? {False}")
print(f"Tu edad en 10 años sera: {edad_futura}")
print(f"La media de tu edad actual y tu edad en 20 años es {media}")
