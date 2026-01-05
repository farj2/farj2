#Uso de def ():
def saludo():
    """el docstring es hacer 
    comentarios justo después del def
    para ayudar a explicar la función"""
    print("¡Hola, Mundo!")
    
saludo()


#Uso de función len()
lista=[1,2,3,4,5,6,7,8,9,10]
longitud=len(lista)
print(longitud)


#Uso de input() y print()
nombre=input("Cuál es tu nombre?")
print("Hola, ",nombre)


#Uso de función type()
x=10
y="Hola"
z=[1,2,3]
print(type(x))
print(type(y))
print(type(z))


#Conversión de str a int
numero_texto="123"
numero=int(numero_texto)
print(numero+10)
#Conversión de int a str
numeroo="456"
texto=str(numeroo)
print("El numero es "+numeroo)


#Ejemplo de función personalizada
def cuadrado(numerooo):
    """ Calcula el cuadrado de un número.
    Args:
    numerooo: El número a elevar al cuadrado
    Returns: El cuadrado del número """
    return numerooo**2

resultado=cuadrado(5)
print(resultado)
#Otro ejemplo
def suma(a,b):
    return a+b
print(suma(5,5))


#Con parámetros predeterminados
def saludo(nombre="Administrador"):
    print("Hola, ", nombre)
saludo()       #sin parámetro
saludo("Ana")  #con parámetro


#Traer de otro archivo
import operaciones #este es otro código que se llama "operaciones.py"
resuultado = operaciones.restar(5,3) #llama la función restar del script operaciones.py
print(resuultado)


#Módulo os
import os
print(os.getcwd()) #Muestra el directorio actual


