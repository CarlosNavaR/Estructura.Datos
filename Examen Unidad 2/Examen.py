import os ## Importo libreria para limpiar pantalla

class Nodo():
	
	def __init__(self,dato):
		self.dato = dato
		self.sig = None
		self.ant = None

class Operaciones():
	
	def __init__(self):
		self.raiz = None
		self.finT = None ## Estara en la ultima posicion y ayudara a recorrer los datos
		self.fin = None
		
	def Null(self): ## Verificara si la lista tiene datos
		if self.raiz == None: ## Se condiciona si el nodo raiz tiene datos
			return True ## Regresa true si se encuentra vacia
		else:
			return False ## False si tiene datos
	
	def Ingresar(self,dato):
		if self.Null() == True: ## Se verifica si la lista esta vacia
			self.raiz = self.fin = Nodo(dato) ## Si esta vacia se les asigna el dato en la primera posicion
		else:
			temporal = self.fin ## Almacena temporalmente el nodo para ligar los datos
			self.finT = self.fin = temporal.sig = Nodo(dato) ## Liga los nodos con la siguiente posicion y almacena el dato
			self.finT.ant = self.fin.ant = temporal ## Liga los nodos con el dato anterior
	
	def RecorrerStart(self): ## Funcion que imprime todos los datos del inicio al fin 
		aux = self.raiz ## Almacena la raiz para recorrer desde el inicio
		if self.Null() == True: ## Se verifica que contenga datos
			print("\n\tNo hay datos registrados...") ## Si no tiene regresa un mensaje 
		else:
			while aux: ## Mientras la raiz contenga datos se ejecutara
				print("\t["+ str(aux.dato)+"]") ## Imprime el dato
				aux = aux.sig ## Avanza al siguiente dato
				
	def RecorrerFin(self): ## Funcion que imprime los datos dede el final al principio
		aux = self.fin ## Se almacena el nodo final
		if self.Null() == True: ## Se verifica que contenga datos
			print("\n\tNo hay datos registrados...") ## Si no tiene regresa un mensaje 
		else:
			while  aux:## Mientras el final contenga datos se ejecutara
				print("\t["+ str(aux.dato)+"]") ## Imprime el dato
				aux = aux.ant ## Retrocede un dato
	
	def Buscar(self,item): ## Funcion que recibe un parametro y lo busca entre los datos almacenados
		temp = self.raiz ## Variable que regresa la variable finT a la raiz y la almacena
		i = False ## Variable que controla si existe el dato o no
		while temp:  ## Mientras la variable temporal se diferente a nulo se ejecutara
			if temp.dato == item:  ## Verifica si el parametro coincide con algun dato
				i = True ## SI coincide la variable I torna valor verdadero
				return i ## Regresa el valor
			else:
				temp = temp.sig ## SI no existe el dato avanza una posicion y regresa a comparar
				if temp == self.raiz: ## Verifica que no sea el unico dato
					i = False 
					return i		
					
	def BuscarEliminar(self,item): ## Funcion que busca un elemento y lo elimina
		self.finT = self.raiz ##  Regresa el puntero a la raiz
		temp = 1 ## VAriable temporal que servira para verificar si existe o no el dato
		
		if self.Null() == True: ## Se verifica que la lista no este vacia
			print("\n\tLista vacia")
		else:
			while self.finT.dato != item and temp == 1: ## Se ejecutara el siguiente siempre y cuando el dato no se encuentre y la variable temporal sea 1
				if self.finT.sig != None: ## Se ejecuta siempre y cuando sea diferente a nulo
					aux = self.fin
					aux = self.finT   
					self.finT = self.finT.sig ## Se recorren todos los dato
				else:
					temp = 0
		
			if temp == 0: ## Si el valor de la variable temporal es 0 es por que no se encuentra el dato
				print("\n\tNo existe el elemento que desea eliminar")
			else:
				if self.raiz == self.finT:  ## se verifica si el dato a eliminar es la raiz
					self.raiz = self.finT.sig
				else:
					aux.sig = self.finT.sig ##Recorre el elemento y lo liga dejandolo libre
				self.finT = None ## Se elimina el elemento
				print("\n\tDato eliminado correctamente")

	def EliminarRaiz(self): ## Elimina la raiz que almacena los datos
		if self.Null() == True: ## Se verifica que contenga datos
			print("\n\tNo existe raiz para eliminar...")
		elif self.raiz.sig == None: ## Verifica que la variable temporal sea diferente al fin de la lista
			self.raiz = self.fin = None ## Si no se cumplio la sentencia es por que solo hay un dato y es la raiz y lo elimina
			print("\n\tUnica Raiz ELiminada")
		else:
			self.raiz = self.raiz.sig ## SI contiene datos la raiz es pasada al siguiente dato 
			self.raiz.ant = None
			print("\n\tRaiz ELiminada")

		
examen = Operaciones()
print("\n\tExamen unidad 2: Listas doblemente enlazadas") 
examen.Ingresar(1)	#
examen.Ingresar(2)	#	
examen.Ingresar(3)	#
examen.Ingresar(4)	#
examen.Ingresar(5)	# Inserta los datos bases
examen.Ingresar(6)	#
examen.Ingresar(7)	#
examen.Ingresar(8)	#
examen.Ingresar(9)	#
print("\n\t1.-Inicio a fin")
examen.RecorrerStart() ## Imprime lista de inicio a fin
print("\n\t2.-Fin a inicio")
examen.RecorrerFin() ## Imprime lista de fin a inicio
print("\n\t3.-Insertando los siguientes datos [10,11,13]")
examen.Ingresar(10) #
examen.Ingresar(12) # Ingresa elementos pedidos 
examen.Ingresar(13) #
print("\n\t4.-Elimando los siguientes datos [8,1]")
examen.BuscarEliminar(8) # Busca un dato y lo elimina 
examen.EliminarRaiz() # ELimina la raiz
print("\n\t5.-Nueva raiz [" + str(examen.raiz.dato) + "]")
print("\n\t6.-Recorre lista ambos lados")
print("\n\t-Inicio a fin")
examen.RecorrerStart()   ## Imprime lista de inicio a fin
print("\n\t-Fin a inicio")
examen.RecorrerFin() ## Imprime lista de fin a inicio
print("\n\t7.-Busca los siguientes datos [0,7,8,1]")
print("\n\t[0]")
verificar = examen.Buscar(0) ## Ejecuta la operacion que muestra si un dato existe o no
if verificar == True: ## Si la funcion regresa un verdadero imprime un mensaje que indica que existe el dato de igual manera si no existe
	print("\tDato existente") 
else:
	print("\tNo existe dato")
print("\n\t[7]")
verificar = examen.Buscar(7) ## Ejecuta la operacion que muestra si un dato existe o no
if verificar == True: ## Si la funcion regresa un verdadero imprime un mensaje que indica que existe el dato de igual manera si no existe
	print("\tDato existente") 
else:
	print("\tNo existe dato")
print("\n\t[8]")
verificar = examen.Buscar(8) ## Ejecuta la operacion que muestra si un dato existe o no
if verificar == True: ## Si la funcion regresa un verdadero imprime un mensaje que indica que existe el dato de igual manera si no existe
	print("\tDato existente") 
else:
	print("\tNo existe dato")
print("\n\t[1]")
verificar = examen.Buscar(1) ## Ejecuta la operacion que muestra si un dato existe o no
if verificar == True: ## Si la funcion regresa un verdadero imprime un mensaje que indica que existe el dato de igual manera si no existe
	print("\tDato existente") 
else:
	print("\tNo existe dato")

