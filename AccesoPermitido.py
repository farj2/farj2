nombre=input("Ingresa tu nombre: ")
edad=int(input("Ingresa tu edad (en numero): "))
rol=input("Ingresa tu rol (estudiante, docente, otro): ")

if edad>=18 and (rol == "estudiante" or rol == "docente"):
    print("Acceso concedido, bienvenido "+nombre)
elif edad<18:
    print("Lo siento "+nombre+", acceso denegado")
elif rol!=("estudiante" or "docente"):
    print("Revisa tu rol nuevamente")