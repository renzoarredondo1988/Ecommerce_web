class Carro:#Importante! los datos obtenidos en una sesion pueden pasar al template directamente!!
    def __init__(self,request):
        self.request=request #almaceno el objeto request en un atributo de instancia llamado self.request. Esto permite acceder al objeto request en otros métodos de la clase Carro.
        self.session=request.session #Esta línea obtiene el objeto session de request. En Django, request.session es un diccionario 
        #que se utiliza para almacenar datos específicos de la sesión del usuario. 
        #Cada usuario tiene su propia sesión, lo que permite almacenar información temporal mientras el usuario navega por tu sitio.
        carro=self.session.get("carro") #"carro" es la clave del dicc que se almacena en la sesion. 
        #En este caso estamos obteniendo todos los atributos que tengan como clave carro. Si no existe ninguno, sera un None
        if not carro:
            carro=self.session["carro"]={} # Si no existe, inicializamos el carrito como un diccionario vacío.
        #ATENCION!!! aqui es donde se esta asignando "carro" como clave del dicc
        self.carro=carro # Aquí asignas el valor de carro (que ahora es el carrito que obtuviste de la sesión, 
        #ya sea el existente o el nuevo vacío) a self.carro. Esto te permite trabajar con el carrito a 
        # través del atributo self.carro en otras partes de la clase. Ojo, carro es una variable local del init,
        #self.carro es una variable de clase, por lo que puedo acceder a traves de metodos.
        

    def agregar(self,producto):#Metodo agregar, recibe como parametro el objeto producto, definido
        #en la funcion agregar_producto de la vista
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id]= {
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":producto.precio,
                "cantidad":1,
                "imagen":producto.imagen.url
                }
            
        else:
            for key,value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio
                    break

        self.guardar_carro()#se guardan los datos de la sesion, lo que hace que persistan los datos al generar
        #nuevas instancias del objeto carro.

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self,producto):
        producto.id=str(producto.id)

        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self,producto): 
        
        for key,value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"])-float(producto.precio)
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break

        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True


  

           
      
        
            
