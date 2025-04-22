# La tienda del buhonero de residen evil 4

class Objeto():     # Creamos la clase objeto, que tendra valores basicos como el nombre y precios de compra y venta.
    def __init__(self,nombre,p_compra):
        self.nombre=nombre
        self.p_compra=p_compra      #Esto es el precio que el buhonero vende al personaje (p de compra para el personaje)
        self.p_venta=p_compra*0.75  #Esto es el precio que el personaje vende al buhonero (p de venta para el personaje)

    def inv_buhonero(self, inventario, cantidad):    # El inventario del negocio recibira dos listas, los inventarios de cosas y la cantidad de cada una de ellas. 
        indice=inventario.index(self)   # Como la cantidad esta en otra lista necesitamos saber el indice del nombre para buscarlo en el inventario de objeto
        print(f"{self.nombre} x {cantidad[indice]} ($ {self.p_compra})")
        
    def inv_leon(self, inventario,cantidad):
        # Leon es el personaje de RE4, mostraremos los items con el precio de venta
        indice=inventario.index(self)
        print(f"{self.nombre} x {cantidad[indice]} ($ {self.p_venta})")



class Arma(Objeto):
    def __init__(self, nombre, p_compra, daño, velocidad_recarga, cadencia, capacidad):
        super().__init__(nombre, p_compra)
        self.daño=daño
        self.velocidad_recarga=velocidad_recarga
        self.cadencia=cadencia
        self.capacidad=capacidad
    
    # def inv_buhonero(self, inventario, cantidad):   #aun no se ocupa el inventario cantidad, sera posible sacarlo? para que me sirve que este aqui? anotar respuesta plis
         
    #     print("  Daño    Vel. recarga    Cadencia    Capacidad")
    #     print("  "+"|"*self.daño+"-"*(6-self.daño), end="   ")
    #     print("|"*self.velocidad_recarga+"-"*(3-self.velocidad_recarga), end="             ")
    #     print("|"*self.cadencia+"-"*(3-self.cadencia), end="         ")
    #     print("|"*self.capacidad+"-"*(6-self.capacidad))

    def inv_buhonero(self, inventario, cantidad):
        super().inv_buhonero(inventario, cantidad)
        print("  Daño    Vel. recarga    Cadencia    Capacidad")
        print("  "+"|"*self.daño+"-"*(6-self.daño), end="   ")
        print("|"*self.velocidad_recarga+"-"*(3-self.velocidad_recarga), end="             ")
        print("|"*self.cadencia+"-"*(3-self.cadencia), end="         ")
        print("|"*self.capacidad+"-"*(6-self.capacidad))
    
    def inv_mejora(self):
        # muestra las estadisticas del arma en el menu de mejora, esto haciendo alucion al juego, puede modificarse
        # OJO, todo esto se hace solo probando a un objeto a la vez, y si funciona, despues se podran hacer cadenas de funcionamiento para que muestre todo o mas de una
        # Esa es la gracia de todo esto... mientras te pueda hacer un objeto y leerlo correctamente, genial, el resto es como accedes despues
        print("Mejorar",self.nombre)

        print("1. Daño             " + "|"*self.daño+"-"*(6-self.daño), end=" "*4)
        print("$ ",10000 - 8000*(1-self.daño/5))    #en este caso es 5 porque se tiene que considerar un nivel menos que el maximo (que es 6)
        print("2. Vel. de recarga: " + "|"*self.velocidad_recarga+"-"*(3-self.velocidad_recarga), end=" "*7)
        print("$ ",10000 - 8000*(1-self.velocidad_recarga/2)) #en este caso es 2 porque se tiene que considerar un nivel menos que el maximo (que es 3)
        print("3. Cadencia:        " + "|"*self.cadencia+"-"*(3-self.cadencia), end=" "*7)
        print("$ ",10000 - 8000*(1-self.cadencia/2)) #en este caso es 2 porque se tiene que considerar un nivel menos que el maximo (que es 3)
        print("4. Capacidad:       " + "|"*self.capacidad+"-"*(6-self.capacidad), end=" "*4)
        print("$ ",10000 - 8000*(1-self.capacidad/5))    #en este caso es 5 porque se tiene que considerar un nivel menos que el maximo (que es 6)
        

class Leon():
    def __init__(self,inventario,cantidad,dinero):
        self.inventario=inventario
        self.cantidad=cantidad
        self.dinero=dinero

    def vender(self, buhonero):
        # mostrar los items con el precio que lo vende y escoger un item
        # sumar precio de venta a dinero y gestionar estado de item en inventario cantidad 
        continuar = True
        posee = False   # con esto es para que si un item no lo tenia el buhonero, entonces si se lo vendemos, se lo agregamos.
        while continuar == True:
            n = 1
            print("-------------} INVENTARIO {--------------")
            print("\nDinero: ",self.dinero)
            for item in self.inventario:
                print(f"{n}. ",end=" ")
                item.inv_leon(self.inventario,self.cantidad)  # como vamos a recorrer cada item en el inventario, y estos son de la clase Objeto, vamos a acceder al metodo de mostrar
                # que en ese caso lo llamamos "inv_leon". Con esto lo mostraremos, pero ademas necesitamos que salgan numerados, asi el jugador los puede seleccionar.
                n += 1 # luego esto simplemente nos enumera la lista... (mirar fuera del for, bajo el while)
            print(len(self.inventario)+1, ". Volver") # esta es el numero de opcion para salir
            opcion= int(input("Vender: "))

            if opcion==len(self.inventario)+1: # si seleccionamos salir, entonces sale de vender
                continuar=False
                break
            
            #entonces ahora tengo que restar el item del inventario (fijarme en la cantidad) y tengo que sumar el dinero al monto total de dinero
            self.cantidad[opcion-1] -=1 # restamos pero ahora falta ver que si el item tiene cantidad cero, entonces que no se muestre, sera aqui? o en otra parte? (mas abajo)
            self.dinero+= self.inventario[opcion-1].p_venta # precio de venta de objeto de la seleccion (opcion) menos 1, ya que la lista parte en 0
            # lo anterior tambien se pudo haber escrito como "self.dinero += obj.p_venta", pero tendriamos que declarar esa variable antes (esta abajo)

            obj = self.inventario[opcion-1]    
            for i in buhonero.inv_tienda: # para cada item en el inventario de la tienda, recorreremos la tienda completa para ver si tiene el inventario o no
                if i == obj: # si uno de los objetos de la lista de buhonero es igual a uno que elegimos nosotros a vender, entonces tiene el item y se lo tenemos que sumar
                    buhonero.cantidad[buhonero.inv_tienda.index(i)] +=1   # posicion del item que elegimos en la lista del buhonero 
                    posee=True # si lo encuentra entonces salimos de este for
                    break
            if posee==False: # con esto hacemos que el objeto se agregue al inventario del buhonero (de la tienda) y que se ponga al final (ya que no lo tiene)
                buhonero.inv_tienda.append(obj)
                buhonero.cantidad.append(1) # con esto hacemos que se 

            indice=self.inventario.index(obj)   # con este metodo decimos que si la cosa llega a cero, entonces se elimina de la lista, tanto el objeto como la cantidad.
            if self.cantidad[indice]==0:            # EL PROFE PUSO ITEM ENTRE PARENTESIS, PERO CREO QUE ES "obj"
                del self.inventario[indice]           # era OBJ, cuando hacia buhonero lo dejo bien, aun no lo cambia. 
                del self.cantidad[indice]    

class Buhonero():
    def __init__(self,inv_tienda,cantidad):
        self.inv_tienda=inv_tienda
        self.cantidad=cantidad

    def vender(self, leon): # mostrar los items con el precio de compra y escoger un item, ademas, verificar si leon puede comprar, 
                  # tambien necesitamos restar p compra a dinero de leon y verificar estado del item en las listas contenedoras de acuerdo a esto gestionar el nuevo estado del item
        continuar =True
        posee=False
        while continuar == True:
            
            n = 1
            print("-------------} TIENDA {--------------")
            print("\nDinero: ",leon.dinero)
            for item in self.inv_tienda:
                print(f"{n}. ",end=" ")
                item.inv_buhonero(self.inv_tienda,self.cantidad)  # como vamos a recorrer cada item en el inventario, y estos son de la clase Objeto, vamos a acceder al metodo de mostrar
                # que en ese caso lo llamamos "inv_buhonero". Con esto lo mostraremos, pero ademas necesitamos que salgan numerados, asi el jugador los puede seleccionar.
                n += 1 # luego esto simplemente nos enumera la lista... (mirar fuera del for, bajo el while)
            print(len(self.inv_tienda)+1, ". Volver") # esta es el numero de opcion para salir
            opcion= int(input("Comprar: "))

            if opcion==len(self.inv_tienda)+1: # si seleccionamos salir, entonces sale de vender
                continuar=False
                break

            obj= self.inv_tienda[opcion-1]
            indice= self.inv_tienda.index(obj)

            if leon.dinero >= obj.p_compra: # recuerda que leon puede ser subtituido como "personaje" | Aqui si leon puede pagar la wea entonces se ejecuta todo lo siguiente
                leon.dinero -= obj.p_compra # a leon le restamos el precio de compra.
                
                for i in leon.inventario: # si el objeto esta en inventario de leon, entonces le sumamos uno y si no, se lo agregamos 
                    if i == obj: # si el objeto elegido antes es igual a alguno del inventario entonces:
                        leon.cantidad[leon.inventario.index(i)] += 1 #agregamos uno al leon
                        self.cantidad[indice] -=1 # y le quitamos uno a la cantidad
                        posee=True # ahora le decimos que lo posee y salimos de la revision
                        break                 
            elif posee==False:# si no lo tiene se lo agregamos
                leon.inventario.append(obj)
                leon.cantidad.append(1)
                self.cantidad[indice] -=1 # le quitamos uno a la cantidad

            elif self.cantidad[indice] == 0:
                del self.inv_tienda[indice]
                del self.cantidad[indice]
            else:
                print("\nDinero insuficiente")
                
    def mejorar(self,leon): # mostrar las armas de leon y permitir seleccionar una, mostrar las estadisticas del arma seleccionada
                    # permitir seleccionar una estadistica a mejorar mostrando su precio, verificar que pueda comprar, restar al dinero de leon y aumentar la estadistica. 
        continuar=True
        while continuar==True:
            print("-----------------MEJORAR----------------")
            print("\nDinero: ",leon.dinero)
            n=1
            for i in leon.inventario: # necesitamos revisar el inventario de leon, y para eso necesitamos que sean solo las armas
                if isinstance(i,Arma)==True:  # con este metodo podemos solo repasar las clases descritas en el parentesis, en este caso Armas
                    print(f"{n}. ", end="") 
                    i.inv_buhonero(leon.inventario,leon.cantidad)
                    print("\n")
                    n+=1
            print(n,". Volver")
            opcion=int(input("Seleccion: "))

            if opcion == n:
                continuar=False
                break

            num_arma=0    
            for i in leon.inventario:
                if isinstance(i,Arma) == True:
                    num_arma+=1
                if isinstance(i,Arma) == True and num_arma==opcion: # todo esto es para ubicar el arma, ya que no tenemos donde buscarla, simplemente nos muestra en la lista, pero esto nos ahorra esa dificultad
                    print("-----------------MEJORAR----------------")
                    print("\nDinero: ",leon.dinero)
                    i.inv_mejora()
                    mejora = int(input("Seleccion: "))
                    if mejora == 5:
                        break
                    if mejora == 1:  # elige el daño
                        if i.daño<6:
                            precio = 10000 - 8000*(1-i.daño/5)
                            if leon.dinero>=precio:
                                leon.dinero-=precio
                                i.daño+=1
                            else:
                                print("Dinero Insuficiente")
                        else:
                            print("Daño mejorado al maximo")              
                    if mejora == 2:  # elige mejorar la velocidad de recarga
                        if i.velocidad_recarga<3:
                            precio = 10000 - 8000*(1-i.daño/2)
                            if leon.dinero>=precio:
                                leon.dinero-=precio
                                i.velocidad_recarga+=1
                            else:
                                print("Dinero Insuficiente")
                        else:
                            print("Vel. Recarga mejorada al maximo")   
                    if mejora == 3:  # elige mejorar la cadencia
                        if i.cadencia<3:
                            precio = 10000 - 8000*(1-i.daño/2)
                            if leon.dinero>=precio:
                                leon.dinero-=precio
                                i.cadencia+=1
                            else:
                                print("Dinero Insuficiente")
                        else:
                            print("Cadencia mejorada al maximo")
                    if mejora == 4:  # elige mejorar la capacidad
                        if i.capacidad<3:
                            precio = 10000 - 8000*(1-i.daño/2)
                            if leon.dinero>=precio:
                                leon.dinero-=precio
                                i.capacidad+=1
                            else:
                                print("Dinero Insuficiente")
                        else:
                            print("Capacidad mejorada al maximo")
"""---------------------------------------------------------------------------------------------------------------------------------------"""

def tienda_buhonero(buhonero,leon):
    seleccion = 0
    while seleccion !=4:
        print("\n-------------TIENDITA BUHONERO------------------\n\n")
        print(" [1. Comprar ] [2. Vender ] [3. Mejorar ]")
        print("               [4. Salir ] \n\n")
        seleccion=int(input("Seleccion: "))

        if seleccion==1:
            buhonero.vender(leon)
        elif seleccion==2:
            leon.vender(buhonero)
        elif seleccion==3:
            buhonero.mejorar(leon)
        else:
            print("Error digitalicalifrigstialidoso")

"""---------------------------------------------------------------------------------------------------------------------------------------"""

objeto1=Objeto("Manzana",1000)
objeto2=Objeto("Hierba",2000)
objeto3=Arma("Pistola",4500,2,2,2,3)
objeto4=Arma("Magnum", 5000,4,1,1,2)
objeto5=Arma("Escopeta",3500,4,1,1,4)
objeto6=Objeto("Repelente",3000)

inventario=[objeto1,objeto3]    # inventario de prueba generalizado, no es individual, luego se tienen que setear inventarios diferentes para cada uno (asumimos ahora que es de leon)
cantidad_personaje=[3,2]                        # lo mismo que lo anterior

inv_tienda=[objeto4,objeto5,objeto6,objeto1,objeto3]
cantidad_tienda=[1,2,4,5,2]

leon = Leon(inventario,cantidad_personaje,20000)
buhonero = Buhonero(inv_tienda,cantidad_tienda)

# con esto probe que funcionara los inventarios de cada uno.
# objeto1.inv_buhonero(inventario,cantidad_personaje)
# objeto1.inv_leon(inventario,cantidad_personaje)

# con esto probamos las armas y sus mejoras
# objeto3.inv_buhonero(inventario,cantidad_personaje)
# objeto3.inv_mejora()

# probando leon
# leon = Leon(inventario,cantidad_personaje,20000)
# leon.vender(cantidad_personaje)

# probando todo
# leon.vender(buhonero) # funcionando
# buhonero.vender(leon)
# leon.vender(buhonero)
# buhonero.vender(leon)

# buhonero.mejorar(leon)

tienda_buhonero(buhonero,leon)