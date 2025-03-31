# Crear la clase Figuras geométricas con los métodos calc_área() y calc perimetro(). 
# De esta clase, heredar las clases triángulo rectángulo, rectángulo y círculo, y sobrescribir los métodos cale_área() y calc_perimetro() en cada caso.

class Figuras():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def calc_area(self):
        area=self.x*self.y
        print(f"Area Rectangulo: {area}")

    def calc_perimetro(self):
        perimetro=(self.x+self.y)*2
        print(f"Perimetro Rectangulo: {perimetro}")

class Triangulo_Rectangulo(Figuras):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def calc_area(self):
        area=(self.x*self.y)/2
        print(f"Area Triangulo Rectangulo: {area}")

    def calc_perimetro(self):
        hipotenusa=(self.x**2+self.y**2)**(1/2)
        perimetro=self.x+self.y+hipotenusa
        print(f"Perimetro Triangulo Rectangulo: {perimetro}")

class Circulo(Figuras):
    def __init__(self, x):
        super().__init__(x)
    
    def calc_area(self):
        area=3.14*self.x**2
        print(f"Area Circulo: {area}")

    def calc_perimetro(self):
        perimetro=2*3.14*self.x
        print(f"Perimetro Circulo: {perimetro}")   

