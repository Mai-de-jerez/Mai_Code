class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}"


class SistemaClientes:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nombre} agregado exitosamente.")

    def eliminar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                self.clientes.remove(cliente)
                print(f"Cliente {nombre} eliminado exitosamente.")
                return
        print(f"No se encontró el cliente {nombre}.")

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente
        return None

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            print("Lista de clientes:")
            for cliente in self.clientes:
                print(cliente)


def main():
    sistema = SistemaClientes()

    while True:
        print("\nSistema de Gestión de Clientes")
        print("1. Agregar un cliente")
        print("2. Eliminar un cliente")
        print("3. Buscar un cliente")
        print("4. Listar todos los clientes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del cliente: ")
            email = input("Ingrese el email del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            cliente = Cliente(nombre, email, telefono)
            sistema.agregar_cliente(cliente)

        elif opcion == '2':
            nombre = input("Ingrese el nombre del cliente a eliminar: ")
            sistema.eliminar_cliente(nombre)

        elif opcion == '3':
            nombre = input("Ingrese el nombre del cliente a buscar: ")
            cliente = sistema.buscar_cliente(nombre)
            if cliente:
                print(cliente)
            else:
                print(f"No se encontró el cliente {nombre}.")

        elif opcion == '4':
            sistema.listar_clientes()

        elif opcion == '5':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()