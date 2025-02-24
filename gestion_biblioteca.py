class Libro:
    biblioteca=[]
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.is_disponible = True

    
    def agregar(self):
        Libro.biblioteca.append(self)
        print("Libro agregado exitosamente.")

    def prestar(self):
        if self.is_disponible:
            self.is_disponible = False  # Cambia el estado a no disponible
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if not self.is_disponible:
            self.is_disponible = True  # Cambia el estado a disponible
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")

    @classmethod
    def mostrar(cls):
        if cls.biblioteca:  
            print("Libros en la biblioteca:")
            for libro in cls.biblioteca:
                estado = "disponible" if libro.is_disponible else "no disponible"
                print(f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Estado: {estado}")
        else:
            print("No hay libros en la biblioteca.")

    @classmethod
    def buscar(cls, isbn):
        # Método para buscar un libro por su ISBN
        for libro in cls.biblioteca:
            if libro.isbn == isbn:
                return libro
        return None

def menu():
    while True:
        print("\nMenu de Biblioteca:")
        print("1. Agregar un nuevo libro")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Mostrar todos los libros")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").lower()

        if opcion == '1':
            titulo = input("Ingresa el título del libro: ")
            autor = input("Ingresa el autor del libro: ")
            isbn = input("Ingresa el ISBN del libro: ")
            nuevo_libro = Libro(titulo, autor, isbn)
            nuevo_libro.agregar()

        elif opcion == '2':
            isbn = input("Ingresa el ISBN del libro a prestar: ")
            libro = Libro.buscar(isbn)
            if libro:
                libro.prestar()
            else:
                print(f"No se encontró ningún libro con ISBN: {isbn}")

        elif opcion == '3':
            isbn = input("Ingresa el ISBN del libro a devolver: ")
            libro = Libro.buscar(isbn)
            if libro:
                libro.devolver()
            else:
                print(f"No se encontró ningún libro con ISBN: {isbn}")

        elif opcion == '4':
            Libro.mostrar()

        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


# Ejecutar el menú
menu()


   



 


