# La tienda del buhonero de residen evil 4

class Objeto():     # Creamos la clase objeto, que tendra valores basicos como el nombre y precios de compra y venta.
    def __init__(self,nombre,p_compra):
        self.nombre=nombre
        self.p_compra=p_compra
        self.p_venta=p_compra*0.75  #Ya que el buhonero nos vende las cosas mas baratas

    def inv_buhonero(self, inventario,cantidad):    # El inventario del negocio recibira dos listas, los inventarios de cosas y la cantidad de cada una de ellas. 
        indice=inventario.index(self)
        print(f"{self.nombre} x {cantidad[indice]} ($ {self.p_compra})")
        
    def inv_leon():
        # Leon es el personaje de RE4, mostraremos los items con el precio de venta
        pass



class Arma(Objeto):
    def __init__(self, nombre, p_compra,daño,velocidad_ataque,):
        super().__init__(nombre, p_compra)
        

"""---------------------------------------------------------------------------------------------------------------------------------------"""

objeto1=Objeto("Spray",100)
objeto2=Objeto("Hierba",20)
objeto3=Objeto("Granada",200)

inventario=[objeto1,objeto2,objeto3]
cantidad=[3,1,2]

objeto1.inv_buhonero(inventario,cantidad)
