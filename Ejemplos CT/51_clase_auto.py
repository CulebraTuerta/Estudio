# Hacer una clase auto con los atributos: color, placa, marca y precio.
# Además del método: mostrar atributos() y calcular impuesto() que será del 1% del precio.
 
class Auto():
    def __init__(self,color,placa,marca,precio):
        self.color=color
        self.placa=placa
        self.marca=marca
        self.precio=precio
    
    def mostrar_atributos(self):
        print(f"Los atributos son: {self.color} / {self.placa} / {self.marca}")

    def calcular_impuestos(self):
        impuestos=self.precio*0.01
        print(f"Los impuestos a pagar son ${impuestos} euros")

auto=Auto("Rojo","XXX-666","BMW",45000)

auto.mostrar_atributos()
auto.calcular_impuestos()
