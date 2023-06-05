class Bebida:
    def __init__(self, id, nombre, clasificacion, marca, precio):
        self.id = id
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca
        self.precio = precio


class AlmacenBebidas:
    def __init__(self):
        self.bebidas = []

    def add_bebida(self, bebida):
        self.bebidas.append(bebida)

    def del_bebida(self, id):
        self.bebidas = [bebida for bebida in self.bebidas if bebida.id != id]

    def upd_bebida(self, id, nombre, clasificacion, marca, precio):
        for bebida in self.bebidas:
            if bebida.id == id:
                bebida.nombre = nombre
                bebida.clasificacion = clasificacion
                bebida.marca = marca
                bebida.precio = precio
                break

    def show_bebidas(self):
        for bebida in self.bebidas:
            print(f"ID: {bebida.id}")
            print(f"Nombre: {bebida.nombre}")
            print(f"Clasificación: {bebida.clasificacion}")
            print(f"Marca: {bebida.marca}")
            print(f"Precio: {bebida.precio}")
            print("--------------------------")

    def calc_precioprom(self):
        total = sum(bebida.precio for bebida in self.bebidas)
        promedio = total / len(self.bebidas)
        return promedio

    def cant_pormarca(self, marca):
        cantidad = sum(1 for bebida in self.bebidas if bebida.marca == marca)
        return cantidad

    def cant_porclasif(self, clasificacion):
        cantidad = sum(1 for bebida in self.bebidas if bebida.clasificacion == clasificacion)
        return cantidad

def mostrar_menu():
    print("----- MENÚ -----")
    print("1. Agregar bebida")
    print("2. Eliminar bebida")
    print("3. Actualizar bebida")
    print("4. Mostrar todas las bebidas")
    print("5. Calcular precio promedio de bebidas")
    print("6. Cantidad de bebidas de una marca")
    print("7. Cantidad de bebidas por clasificación")
    print("8. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def agregar_bebida():
    id = int(input("Ingrese el ID de la bebida: "))
    nombre = input("Ingrese el nombre de la bebida: ")
    clasificacion = input("Ingrese la clasificación de la bebida: ")
    marca = input("Ingrese la marca de la bebida: ")
    precio = float(input("Ingrese el precio de la bebida: "))
    bebida = Bebida(id, nombre, clasificacion, marca, precio)
    almacen.add_bebida(bebida)
    print("Bebida agregada correctamente.")

def eliminar_bebida():
    id = int(input("Ingrese el ID de la bebida a eliminar: "))
    almacen.del_bebida(id)
    print("Bebida eliminada correctamente.")

def actualizar_bebida():
    id = int(input("Ingrese el ID de la bebida a actualizar: "))
    nombre = input("Ingrese el nuevo nombre de la bebida: ")
    clasificacion = input("Ingrese la nueva clasificación de la bebida: ")
    marca = input("Ingrese la nueva marca de la bebida: ")
    precio = float(input("Ingrese el nuevo precio de la bebida: "))
    almacen.upd_bebida(id, nombre, clasificacion, marca, precio)
    print("Bebida actualizada correctamente.")

def mostrar_bebidas():
    print("----- BEBIDAS -----")
    almacen.show_bebidas()

def calcular_precio_promedio():
    promedio = almacen.calc_precioprom()
    print(f"Precio promedio de bebidas: {promedio}")

def cantidad_por_marca():
    marca = input("Ingrese el nombre de la marca: ")
    cantidad = almacen.cant_pormarca(marca)
    print(f"Cantidad de bebidas de la marca '{marca}': {cantidad}")

def cantidad_por_clasificacion():
    clasificacion = input("Ingrese la clasificación: ")
    cantidad = almacen.cant_porclasif(clasificacion)
    print(f"Cantidad de bebidas de la clasificación '{clasificacion}': {cantidad}")

almacen = AlmacenBebidas()

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        agregar_bebida()
    elif opcion == "2":
        eliminar_bebida()
    elif opcion == "3":
        actualizar_bebida()
    elif opcion == "4":
        mostrar_bebidas()
    elif opcion == "5":
        calcular_precio_promedio()
    elif opcion == "6":
        cantidad_por_marca()
    elif opcion == "7":
        cantidad_por_clasificacion()
    elif opcion == "8":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
