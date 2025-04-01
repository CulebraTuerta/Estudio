# Implementar clases

class Libro():
    def __init__(self,titulo,autor,ISBN,estado):
        self.titulo=titulo
        self.autor=autor
        self.ISBN=ISBN
        self.estado=estado

    def datos(self):
        print("\nTitulo: ",self.titulo)
        print("Autor: ",self.autor)
        print("ISBN:" ,self.ISBN)
        if self.estado == True:
            print("Estado: Disponible")
        else:
            print("Estado: Prestado")

class Biblioteca():
    def __init__(self,libros):  # Se le entregara una lista de libros
        self.libros=libros

    def buscar_libros(self,nombre_libro):
        print("Buscando Libros")
        for libro in self.libros:   # Para una variable "libro" en lista libros
            if nombre_libro.upper() == libro.titulo.upper():  # busco el nombre del libro en mayusculas en la lista, que contendra objetos libros, por eso estoy llamando al comando titulo
                print("\nLibro encontrado")
                libro.datos()   # recordar que este libro, hace referencia a la variable del for, que a su vez es lo que recorre la lista de libros entregada a esta clase 
                                # pero libro hace referencia a un objeto de clase libro, por lo cual podemos llamar a datos()
            else:
                print("\nLibro no encontrado")
            
    def prestados(self):
        print("Libros prestados")
        for libro in self.libros:
            if libro.estado==False:
                libro.datos()
                print("\n")

class Persona():
    def __init__(self,nombre,codigo):
        self.nombre=nombre
        self.codigo=codigo
        self.libros_prestados=[]

    def prestar(self,biblioteca):
        print("Libros Disponibles")
        for libro in biblioteca.libros:
            if libro.estado == True:
                libro.datos()
                print("\n")
        seleccion=input("Ingrese el nombre del libro a solicitar: ")
        for libro in biblioteca.libros:
            if seleccion.upper()== libro.titulo.upper():
                self.libros_prestados.append(libro)
                libro.estado=False
                print("Libro prestado correctamente")
                break
        
    def devolver(self):
        print("Libros en prestamo, a devolver")
        for libro in self.libros_prestados:
            libro.datos()
            print("\n")

        seleccion=input("Ingrese el nombre del libro a devolver: ")
        for libro in self.libros_prestados:
            if seleccion.upper()== libro.titulo.upper():
                libro.estado=True
                del self.libros_prestados[self.libros_prestados.index(libro)]
                print("Libro devuelto correctamente")
                break

don_quijote = Libro("Don Quijote", "Miguel de Cervantes", 6846834698798, True)  # El comando true al final significa que esta disponible.
harry_potter = Libro("Harry Potter", "JK Rowling", 3123125126544, True)
cien_años = Libro("Cien años de soledad", "Gabriel Garcia Marquez", 6546532165874, True )

libros=[don_quijote,harry_potter,cien_años]    # Creo la lista con los libros de la biblioteca

biblioteca=Biblioteca(libros)   # Creo la biblioteca con la lista de los libros disponibles
danny=Persona("Danny",541654)

danny.prestar(biblioteca)
# biblioteca.buscar_libros("don quijote")
biblioteca.prestados()
danny.devolver()
biblioteca.prestados()



