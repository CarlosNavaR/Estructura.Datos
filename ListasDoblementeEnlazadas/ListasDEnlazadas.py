import os ## Importo libreria para limpiar pantalla

class Nodo():
	
	def __init__(self,dato):
		self.dato = dato
		self.sig = None
		self.ant = None

class Operaciones():
	
	def __init__(self):
		self.raiz = None
		self.fin = None
		
	def Null(self): ## Verificara si la lista tiene datos
		if self.raiz == None: ## Se condiciona si el nodo raiz tiene datos
			return True ## Regresa true si se encuentra vacia
		else:
			return False ## False si tiene datos
			
	def IngresarInicio(self,dato):
		if self.Null() == True: ## Se verifica si la lista esta vacia
			self.raiz = self.fin = Nodo(dato) ## Si esta vacia se les asigna el dato en la primera posicion
		else: 
			temp = Nodo(dato) ## Almacena el dato para poder insertarlo al inicio
			temp.sig = self.raiz ## Enlaza el dato el siguiente nodo sea la raiz 
			self.raiz.ant = temp ## Enlaza que la raiz que sea el anterior dato
			self.raiz = temp ## Le asigna el valor a la raiz
					
	
	def Ingresar(self,dato):
		if self.Null() == True: ## Se verifica si la lista esta vacia
			self.raiz = self.fin = Nodo(dato) ## Si esta vacia se les asigna el dato en la primera posicion
		else:
			temporal = self.fin ## Almacena temporalmente el nodo para ligar los datos
			self.fin = temporal.sig = Nodo(dato) ## Liga los nodos con la siguiente posicion y almacena el dato
			self.fin.ant = temporal ## Liga los nodos con el dato anterior
	
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
	#
	#
	#
	# Crear metodo buscar y eliminar
	#
	#
	

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
		

	def Eliminar(self): ## Esta funcion permite eliminar el ultimo nodo de la lista
		if self.Null() == True: ## Verifica si contiene datos
			print("\n\tNo hay datos para eliminar...")
		elif self.raiz.sig == None: ## Verifica que la variable temporal sea diferente al fin de la lista
			self.raiz = self.fin = None ## Si no se cumplio la sentencia es por que solo hay un dato y es la raiz y lo elimina
			print("\n\tUltimo dato eliminado")
		else:
			self.fin = self.fin.ant
			self.fin.sig = None
			print("\n\tDato eliminado")
		

class  Menu(): ## Clase que controlara las operaciones y lo que se mostrara en consola
	
	def __init__(self): ## Inicia las variables que se usaran
		self.opc = None
		
	def capturar(self): ## Funcion que muestra datos en pantalla y pide los datos
		captura = Operaciones() ## hace referencia a la clase que contiene las operaciones para poder ser usadas
		while True: ## Se crea un ciclo while siempre en verdadero para que se ejecute infinitamente
			print("\n0.-Almacenar por el inicio\n1.-Almacenar datos final\n2.-Mostrar datos de inicio a fin\n3.-Mostrar datos de final a inicio\n4.-Buscar elemento\n5.-Eliminar datos\n6.-Eliminar raiz\n7.-Buscar dato y eliminarlo\n8.-Salir")
			self.opc = int(input("\n\tIngrese opcion -> ")) ## Se imprimen las operaciones y se captura una opcion
			os.system("clear") ## Limpia la pantalla
			
			if self.opc == 0:
				x = int(input("\n\tIngresa dato: ")) ## pide un dato y lo manda como parametro para ser almacenado
				captura.IngresarInicio(x)
			elif self.opc == 1:
				x = int(input("\n\tIngresa dato: ")) ## pide un dato y lo manda como parametro para ser almacenado
				captura.Ingresar(x)
			
			elif self.opc == 2:
				captura.RecorrerStart()
				
			elif self.opc == 3:
				captura.RecorrerFin()
				
			elif self.opc == 4:
				date = int(input("\n\tIngresa dato a buscar: "))
				verificar = captura.Buscar(date) ## Ejecuta la operacion que muestra si un dato existe o no
				if verificar == True: ## Si la funcion regresa un verdadero imprime un mensaje que indica que existe el dato de igual manera si no existe
					print("\n\tDato existente") 
				else:
					print("\n\tNo existe dato")
					
			elif self.opc == 5:
				captura.Eliminar() ## Ejecuta la operacion que elimina elementos de atras adelante
			
			elif self.opc == 6:
				captura.EliminarRaiz()
			
			elif self.opc == 7:
				dato = int(input("\n\tIngresa dato a eliminar: "))
				captura.BuscarEliminar(dato) ## Ejecuta la operacion que busca un dato y lo elimina
					
			elif self.opc == 8:
				exit() ## Se sale del programa
				
			else: ## Si ingresa una opcion que no se encuentra en el menu ejecuta un mensaje que indica que es una opcion invalida
				print("\n\tOpcion invalida")


Imprimir = Menu() ## Hace referencia a la clase que contiene el menu para poder ser llamado
Imprimir.capturar() ## Imprime el menu