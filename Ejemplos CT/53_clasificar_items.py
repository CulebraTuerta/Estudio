# Hacer un programa que permita clasificar los ítems de una tienda, 
# se deberá recibir un inventario con un número de ítems y 
# dividirlos en 3 grupos: comida, herramientas y aseo

class Producto():
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
    
    def datos(self):
        print(f"{self.nombre}: {self.precio}")

class Comida(Producto):
    def __init__(self, nombre, precio, caducidad):
        super().__init__(nombre, precio)
        self.caducidad=caducidad
    
    def datos(self):
        print(f"{self.nombre}: {self.precio} / Caducidad {self.caducidad}")

class Herramienta(Producto):
    def __init__(self, nombre, precio, material):
        super().__init__(nombre, precio)
        self.material=material
    
    def datos(self):
        print(f"{self.nombre}: {self.precio} / Material {self.material}")

class Aseo(Producto):
    def __init__(self, nombre, precio, uso):
        super().__init__(nombre, precio)
        self.uso=uso
    
    def datos(self):
        print(f"{self.nombre}: {self.precio} / Uso {self.uso}")


class Tienda():
    def __init__(self, inventario):
        self.inventario=inventario

    def comida(self):
        print("clasificando comida")
        for item in self.inventario:
            if isinstance(item,Comida) == True:
                item.datos()
                print("\n")

    def herramienta(self):
        print("clasificando herramienta")
        for item in self.inventario:
            if isinstance(item,Herramienta) == True:
                item.datos()
                print("\n")

    def aseo(self):
        print("clasificando aseo")
        for item in self.inventario:
            if isinstance(item,Aseo) == True:
                item.datos()
                print("\n")

manzana = Comida ("Manzana", 3000, "22/03/24")
pera = Comida("Pera", 4000, "25/03/24")
chocolate = Comida( "Chocolate", 2500, "12/07/24")
martillo = Herramienta ("Martillo", 45000, "Metal")
destornillador = Herramienta("Destornillador", 37000, "Metal y plástico")
detergente = Aseo("Detergente", 7000, "1 tapa de detergente por cada 5 litros de agua")
inventario = [manzana, destornillador, detergente, chocolate,martillo,pera]

tiendita=Tienda(inventario)

tiendita.comida()
tiendita.herramienta()
tiendita.aseo()
