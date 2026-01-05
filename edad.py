#SOLICITUDES AL USUARIO
edad=int(input("Ingresa tu edad: "))
rol=input("Ingresa tu rol (estudiante, docente, visitante): ")

#CLASIFICAR EDAD
if edad<13:
    usuario="Infancia"
elif edad>=13 and edad<17:
    usuario="Adolescencia"
elif edad>=18 and edad<64:
    usuario="Adultez"
    else usuario="Persona mayor"
