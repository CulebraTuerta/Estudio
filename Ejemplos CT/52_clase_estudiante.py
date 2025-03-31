# Implementar la siguiente clase
# ESTUDIANTE
# - Nombre
# - Código
# Asignatura
# Nota 1
# Nota 2
# Nota 3
# Nota 4
# - Mostrar datos( )
# - Calificación( )

class Estudiante():
    def __init__(self,nombre,codigo,asignatura,n1,n2,n3,n4):
        self.nombre=nombre
        self.codigo=codigo
        self.asignatura=asignatura
        self.nota1=n1
        self.nota2=n2
        self.nota3=n3
        self.nota4=n4

    def mostrar_datos(self):
        print("\nDatos del estudiante")
        print(f"Nombre: {self.nombre}")
        print(f"Codigo: {self.codigo}")
        print(f"Asignatura: {self.asignatura}")

    def calificacion(self):
        promedio=round((self.nota1+self.nota2+self.nota3+self.nota4)/4)
        print(f"\nPromedio: {promedio}")
    
danny=Estudiante("Danny",17566,"Programacion",57,64,67,59)

danny.mostrar_datos()
danny.calificacion()
