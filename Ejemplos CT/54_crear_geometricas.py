# Crear la clase Figuras geométricas con los métodos calc_área() y calc perimetro(). 
# De esta clase, heredar las clases triángulo rectángulo, rectángulo y círculo, y sobrescribir los métodos cale_área() y calc_perimetro() en cada caso.
from math import pi # con esto importamos el valor de pi, si necesitamos todas las matematicas usamos from math import *

class Figuras():
    def __init__(self,figura):
        self.figura=figura
    
    def calc_area(self):
        pass

    def calc_perimetro(self):
        pass

class Rectangulo(Figuras):
    def __init__(self, figura,ladox,ladoy):
        super().__init__(figura)
        self.ladox=ladox
        self.ladoy=ladoy    

    def calc_area(self):
        area=self.ladox*self.ladoy
        print(f"Area Rectangulo: {area}")
    
    def calc_perimetro(self):
        perimetro=(self.ladox+self.ladoy)*2
        print(f"Perimetro Rectangulo: {perimetro}")

class Triangulo_Rectangulo(Figuras):
    def __init__(self,figura,base,altura):
        super().__init__(figura)
        self.base=base
        self.altura=altura
    
    def calc_area(self):
        area=(self.base*self.altura)/2
        print(f"Area Triangulo Rectangulo: {area}")

    def calc_perimetro(self):
        hipotenusa=(self.base**2+self.altura**2)**(1/2)
        perimetro=self.base+self.altura+hipotenusa
        print(f"Perimetro Triangulo Rectangulo: {perimetro}")

class Circulo(Figuras):
    def __init__(self,figura,radio):
        super().__init__(figura)
        self.radio=radio
    
    def calc_area(self):
        area=pi*self.radio**2
        print(f"Area Circulo: {area}")

    def calc_perimetro(self):
        perimetro=2*pi*self.radio
        print(f"Perimetro Circulo: {perimetro}")   


figura1=Rectangulo("Rectangulo",3,4)
figura1.calc_area()
figura1.calc_perimetro()

figura2=Triangulo_Rectangulo("Triangulo Rectangulo",3,4)
figura2.calc_area()
figura2.calc_perimetro()

figura3=Circulo("Circulo",2)
figura3.calc_area()
figura3.calc_perimetro()
