# Caracol Express
class Encomienda:
    def _init_(self, nombre_destinatario, rut_destinatario, peso, precio, ciudad):
        self.nombre_destinatario = nombre_destinatario.upper()
        self.rut_destinatario = rut_destinatario.upper()
        self.peso = peso
        self.precio = precio
        self.ciudad = ciudad.upper()

def validar_rut(rut):
    rut = rut.upper()
    if len(rut) >= 2 and rut[-2] == '-':
        return True
    return False

def validar_precio(precio):
    return precio >= 2000

def validar_peso(peso):
    return peso >= 0.1

def validar_ciudad(ciudad):
    return len(ciudad) >= 3

def guardar_encomienda():
    nombre_destinatario = input("Ingrese el nombre del destinatario: ")
    rut_destinatario = input("Ingrese el rut del destinatario: ")
    peso = float(input("Ingrese el peso en kgs: "))
    precio = int(input("Ingrese el precio de la ciudad de destino: "))
    ciudad = input("Ingrese el nombre de la ciudad de destino: ")

    if validar_rut(rut_destinatario) and validar_precio(precio) and validar_peso(peso) and validar_ciudad(ciudad):
        encomienda = Encomienda(nombre_destinatario, rut_destinatario, peso, precio, ciudad)
      
        print("Encomienda guardada exitosamente.")
    else:
        print("Datos de encomienda inválidos. No se pudo guardar.")

while True:
    print("----- Caracol Express -----")
    print("1. Guardar datos de encomienda")
    print("2. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        guardar_encomienda()
    elif opcion == "2":
        print("Gracias por usar Caracol Express. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


#chatgpt no lo necesito si poco a poco estoy pagando un curso de udemy , lo poco que entiendo en clases trato de estudiarlo pagando un curso 
#me queda demasiado aun...