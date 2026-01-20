'''
FELIPE ANDRÉS RAMOS JERIA
Título script: ProyectoModulo2.py
Este código busca resolver la solicitud de la creación de un sistema gestor de contactos 
Desplegando un menú para que el usuario pueda seleccionar entre 
Agregar, Editar, Eliminar o Buscar un contacto
'''
#Creación de los datos de usuarios Nombre, Teléfono, Correo y Dirección
#Además de las funciones de cada uno y la función para print datos en terminal
class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self._nombre = nombre
        self._telefono = telefono
        self._correo = correo
        self._direccion = direccion

    #Se definen los get de los datos
    def get_nombre(self):
        return self._nombre
    def get_telefono(self):
        return self._telefono
    def get_correo(self):
        return self._correo
    def get_direccion(self):
        return self._direccion

    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_telefono(self, telefono):
        self._telefono = telefono
    def set_correo(self, correo):
        self._correo = correo
    def set_direccion(self, direccion):
        self._direccion = direccion
    
    #Se define la función "mostrar" la cual imprime en la terminal los datos de los usuarios
    def mostrar(self):
        return (
            f"Nombre    : {self._nombre}\n"
            f"Teléfono  : {self._telefono}\n"
            f"Correo    : {self._correo}\n"
            f"Dirección : {self._direccion}"
        )

#Creación de la clase GestorContactos, la cual contiene las funciones sobre los datos
class GestorContactos:
    def __init__(self):
        self.contactos = []

    #Función Agregar Contacto que permite anexar un contacto nuevo en la lista de Contacto
    def agregar_contacto(self, nombre, telefono, correo, direccion):
        contacto = Contacto(nombre, telefono, correo, direccion)
        self.contactos.append(contacto)

    #Función Buscar Contacto, esta permite buscar algún contacto según el criterio de Nombre o Teléfono
    def buscar_contacto(self, criterio):
        resultados = []
        for contacto in self.contactos:
            if (criterio.lower() in contacto.get_nombre().lower() or
                criterio == contacto.get_telefono()):
                resultados.append(contacto)
        return resultados

    #Función Editar Contacto, permite editar algún contacto buscando según el Teléfono
    #Para mantener algún dato se requiere dar Enter
    #Para modificar se debe escribir nuevo dato y luego Enter para guardar
    def editar_contacto(self, telefono):
        for contacto in self.contactos:
            if contacto.get_telefono() == telefono:

                print("\n--- Editando contacto ---")
                print(contacto.mostrar())

                nuevo_nombre = input("Nuevo nombre (Enter para mantener): ")
                nuevo_telefono = input("Nuevo teléfono (Enter para mantener): ")
                nuevo_correo = input("Nuevo correo (Enter para mantener): ")
                nueva_direccion = input("Nueva dirección (Enter para mantener): ")

                if nuevo_nombre:
                    contacto.set_nombre(nuevo_nombre)
                if nuevo_telefono:
                    contacto.set_telefono(nuevo_telefono)
                if nuevo_correo:
                    contacto.set_correo(nuevo_correo)
                if nueva_direccion:
                    contacto.set_direccion(nueva_direccion)

                print("\nContacto actualizado correctamente.\n")
                return True

        print("\nContacto no encontrado.\n")
        return False

    #Función Eliminar Contacto, permite eliminar algún contacto buscándolo según Teléfono
    def eliminar_contacto(self, telefono):
        for contacto in self.contactos:
            if contacto.get_telefono() == telefono:
                self.contactos.remove(contacto)
                print("\nContacto eliminado correctamente.\n")
                return True

        print("\nContacto no encontrado.\n")
        return False

    #Función Listar Contactos, muestra en pantalla todos los Contactos guardados para visualizar
    def listar_contactos(self):
        if not self.contactos:
            print("\nNo hay contactos registrados.\n")
            return

        print("\n--- Lista de contactos ---\n")
        for i, contacto in enumerate(self.contactos, start=1):
            print(f"Contacto {i}")
            print(contacto.mostrar())
            print("-" * 30)

#Función Mostrar Menú para dar al usuario una interfaz de las opciones disponibles
# ---------------- MENÚ PRINCIPAL ---------------- #

def mostrar_menu():
    print("\n===== GESTOR DE CONTACTOS =====")
    print("1. Agregar contacto")
    print("2. Editar contacto")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Listar contactos")
    print("6. Salir")


#Función Main, esta llama a todas las opciones del Gestor de Contactos e inicializa el programa
def main():
    gestor = GestorContactos()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\n--- Nuevo contacto ---")
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            direccion = input("Dirección: ")

            gestor.agregar_contacto(nombre, telefono, correo, direccion)
            print("\nContacto agregado correctamente.\n")

        elif opcion == "2":
            telefono = input("\nIngrese el teléfono del contacto a editar: ")
            gestor.editar_contacto(telefono)

        elif opcion == "3":
            telefono = input("\nIngrese el teléfono del contacto a eliminar: ")
            gestor.eliminar_contacto(telefono)

        elif opcion == "4":
            criterio = input("\nIngrese nombre o teléfono a buscar: ")
            resultados = gestor.buscar_contacto(criterio)

            if resultados:
                print("\n--- Resultados encontrados ---\n")
                for contacto in resultados:
                    print(contacto.mostrar())
                    print("-" * 30)
            else:
                print("\nNo se encontraron contactos.\n")

        elif opcion == "5":
            gestor.listar_contactos()

        elif opcion == "6":
            print("\nSaliendo del programa...\n")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.\n")


#Inicia ciclo MAIN
if __name__ == "__main__":
    main()
