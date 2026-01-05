#SOLICITUDES AL USUARIO
edad=int(input("Ingresa tu edad: "))
rol=str(input("Ingresa tu rol (estudiante, docente, visitante): "))

#CLASIFICAR EDAD
edad_usuario="Infancia" if edad<13 elif edad>=13 and edad<17 edad_usuario="Adolescencia" elif edad>=18 and edad<64 edad_usuario="Adultez" else edad_usuario="Persona mayor"