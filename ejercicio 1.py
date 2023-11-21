""" nombre = "juanito"
apellido = "lopez"
edad = 56
# Metodo 1
print ("hola",nombre,"tu apellido es",apellido,"y tenes",edad,"años")
# Metodo 2
print ("hola,{nombre} tu apellido es {apellido} y tenes {edad} años")
# Metodo 3
print (f"hola %s tu apellido es %s y tenes %s años" % (nombre,apellido,edad)) """


#Ejercico 1
""" nombre="hola como estas"
print(nombre)
nombre= "bien y vos"
print (nombre) """

#Ejercicio 2
""" nombre="fede"
print(f"hola {nombre}, ¿te gustaria aprender a programar en pyton?") """

# Ejercico 3
""" ingreso = int(input("ingrese un numero"))
porcentaje = ingreso * 0.15
print (ingreso-porcentaje) """


#Ejercicio 4
""" ingreso = int (input("coloca un numero"))
print(ingreso + 2)

ingreso1 = int(input("ingrese un numero"))
ingreso2 = int(input("ingrese un numero"))
ingreso3 = int(input("ingrese un numero"))
print ((ingreso1+ingreso2+ingreso3)/3) """


# Ejercio 5
""" name=input("ingresa tu nombre:")
edad=int(input("ingresa tu edad:"))
anio=2022+(100-20) #primero resto la edad de la persona a los 100 años y luego los sumo al año actual
print(name+", vas a cumplir 100 años en: ",año) """

# Ejercicio 6
kilogramos = 5
libras = kilogramos * 2.2
print(f"{kilogramos} kg son {libras} lb")

# Ejercicio 7
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit