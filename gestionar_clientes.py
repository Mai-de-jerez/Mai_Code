class Cliente:
    def __init__(self, nombre, email, telefono):
        """
        Inicializa un nuevo cliente con nombre, email y teléfono.
        """
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __str__(self):
        """
        Retorna una representación amigable del cliente.
        """
        return f"{self.nombre} - Email: {self.email}, Tel: {self.telefono}"


class SistemaClientes:
    def __init__(self):
        """
        Inicializa el sistema de gestión de clientes con una lista vacía.
        """
        self.clientes = []

    def agregar_cliente(self, cliente):
        """
        Agrega un nuevo cliente al sistema.
        """
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' agregado al sistema.")

    def eliminar_cliente(self, nombre):
        """
        Elimina un cliente por su nombre.
        """
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                self.clientes.remove(cliente)
                print(f"Cliente '{nombre}' eliminado del sistema.")
                return
        print(f"Cliente '{nombre}' no encontrado en el sistema.")

    def buscar_cliente(self, nombre):
        """
        Busca un cliente por su nombre y retorna el objeto Cliente.
        """
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente
        return None

    def listar_clientes(self):
        """
        Lista todos los clientes disponibles en el sistema.
        """
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente)


def mostrar_menu():
    """
    Muestra el menú principal.
    """
    print("\n" + "="*30)
    print(" Sistema de Gestión de Clientes ")
    print("="*30)
    print("1. Agregar un cliente")
    print("2. Eliminar un cliente")
    print("3. Buscar un cliente")
    print("4. Listar todos los clientes")
    print("5. Salir")
    print("="*30)


def main():
    """
    Función principal que gestiona la interacción con el usuario.
    """
    sistema = SistemaClientes()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            email = input("Ingrese el email del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            cliente = Cliente(nombre, email, telefono)
            sistema.agregar_cliente(cliente)

        elif opcion == "2":
            nombre = input("Ingrese el nombre del cliente a eliminar: ")
            sistema.eliminar_cliente(nombre)

        elif opcion == "3":
            nombre = input("Ingrese el nombre del cliente a buscar: ")
            cliente = sistema.buscar_cliente(nombre)
            if cliente:
                print(f"Cliente encontrado: {cliente}")
            else:
                print(f"Cliente '{nombre}' no encontrado.")

        elif opcion == "4":
            sistema.listar_clientes()

        elif opcion == "5":
            print("Saliendo del sistema de gestión de clientes.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")


if __name__ == "__main__":
    main()
