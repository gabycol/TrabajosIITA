#Diseña una función que tome como parámetro 2 números, y que devuelva una lista 
#que contenga todos los números enteros entre estos 2 incluyendo ambos parámetros.
#Ejemplo: los parámetros para mi función son 1 y 9, por lo tanto, mi función retornara: 
#[1,2,3,4,5,6,7,8,9]

""" def lista_numeros_entre(a, b):
    return list(range(a, b+1))
numeros = lista_numeros_entre(1, 9)
print(numeros)
 """
#Escribir una función que tome como parámetro 2 números, y retorne una lista con 
#todos los números pares entre estos, excluyendo a los parámetros.
#Ejemplo: los parámetros son 4 y 9, por lo tanto, la función retornara: [6,8]

""" def esPar(numero):
    if numero%2==0:
        return True
    return False
def funcion1(param1,param2):
    lista=[]
    for i in range (param1+1,param2):
        if esPar(i):
            lista.append(i)
    return lista
print(funcion1(4,9)) """

#Escribir una función que tome 2 parámetros, el primero que reciba una cadena, y el 
#segundo que reciba un carácter. La función tendrá que retornar la cantidad de veces 
#que aparece ese carácter en esa cadena. 
#Ejemplo: si los parámetros son “Hola mi nombre es Sebastián” y “s”, la función tendrá
#que retornar 3 ya que la s se encuentra 3 veces repetidas en mi cadena.

""" def contar_caracteres(cadena, caracter):
    contador = 0
    for c in cadena:
        if c == caracter:
            contador += 1
    return contador
cadena = "Hola gaby como estas"
caracter = "a"
resultado = contar_caracteres(cadena, caracter)
print(resultado) """

#Elaborar una función que tome como parámetro 2 números, y retorne una lista con
#todos los números primos entre ese rango de números.
#Ejemplo: mis parámetros son 4 y 45, la función tendrá que retornar: [5, 7, 11, 13, 17, 
#19, 23, 29, 31, 37, 41, 43]

""" def encontrar_primos(inicio, fin):
    primos = []
    for num in range(inicio, fin + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primos.append(num)
    return primos
primos = encontrar_primos(7, 85)
print(primos) """

#Elaborar una función que tome como parámetro una lista, y devuelva un bool que diga 
#si en esa lista todos sus números son pares.

""" def todos_pares(lista):
    for numero in lista:
        if numero % 2 != 0:
            return False
    return True
numeros = [2, 4, 6, 8, 10]
resultado = todos_pares(numeros)
print(resultado) """

#Elaborar una función que tome como parámetro una lista y devuelva un bool que diga 
#si en esa lista todos sus números son primos


""" def son_primos(lista):
    for num in lista:
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
    return True
numeros=[2, 3, 5, 7, 11]
resultados= son_primos(numeros)
print(resultados) """


#Elaborar un programa que con un menú el usuario tenga la opción de ingresar una 
#entre 6 opciones.
#a. Para cada opción se tendrá que resolver un punto de los realizados
#anteriormente.
#Por ejemplo, si el usuario selecciona la opción 1 y programa pedirá 2 números, 
#y en base a esos 2 números resolverá el ejerció 1 de esta práctica (devolver y 
#mostrar la lista de números entre ese rango).
#O si por ejemplo el usuario selecciona la opción 3 el usuario tendrá que 
#ingresar una cadena y un carácter y el programa tendrá que mostrar la 
#cantidad de veces que aparece ese carácter en esa cadena.
#Así para cada uno de los puntos

def opcion1():
    print("Hola, bienvenidos!")
def menu():
    print("Opciones disponibles:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Opción 5")
    print("6. Opción 6")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        opcion1()
    elif opcion == 2:
        opcion2()
    elif opcion == 3:
        opcion3()
    elif opcion == 4:
        opcion4()
    elif opcion == 5:
        opcion5()
    elif opcion == 6:
        opcion6()
    else:
        print("Opción inválida. Intente nuevamente.")

def QuitarAlumno(ALUMNO,data):
        
    for elemnto in data["Alumnos"]:
        if elemnto["Nombre"] == ALUMNO:
            data["Alumnos"].remove(elemnto)


DATA = {"Alumnos" : []}

while True:
    print()
    print(DATA)
    print(" 1 : Agreagar alumno")
    print(" 2 : Quitar alumno")
    opcion = int(input("Que haces?:"))
    
    if opcion == 1:
        
        nombre = input("Ingrese un nombre: ")
        edad = input("Ingrese una edad: ")
        alumno = {"Nombre": nombre , "Edad": edad}
        DATA["Alumnos"].append(alumno)
        
    elif opcion == 2:
        QuitarAlumno(input("Que alumno quiere quitar? "),DATA)
    else: 
        print("Opcion invalida")




    