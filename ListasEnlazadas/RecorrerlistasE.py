import os ## Importo libreria para 
class Nodo(): ## Se crea clase nodo que contiene las variables que se usaran para enlazar los datos
	def __init__(self, dato):
		self.dato = dato ## Variable que almacenara los datos
		self.sig = None ## Variable que sera usada como apuntador
	
		
class Operaciones(): ## Se crea una clase que contendra las operaciones a realizar
	
	def __init__(self): ## Se inicializan las variables a utilizar
		self.raiz = None ## Asignara el principio del noto
		self.finT = None ## Estara en la ultima posicion y ayudara a recorrer los datos
		self.fin = None ## Representara el ultimo dato
	
	def Null(self): ## Verificara si la lista tiene datos
		if self.raiz == None: ## Se condiciona si el nodo raiz tiene datos
			return True ## Regresa true si se encuentra vacia
		else:
			return False ## False si tiene datos
		
	def Ingresar(self,dato): ##Funcion que Ingresara datos a la lista
		
		if self.Null() == True: ## Se verifica si la lista esta vacia
			self.raiz = self.finT = self.fin = Nodo(dato) ## Si esta vacia se igualan todos los datos y se les asigna el dato en laprimera posicion
		else:
			temporal = self.fin ## Almacena temporalmente el nodo para ligar los datos
			self.finT = self.fin = temporal.sig = Nodo(dato) ## Liga los nodos con la siguiente posicion y almacena el dato
			
	def Recorrer(self): ## Funcion que recorre los nodos e imprime los datos
		temp = self.raiz ## Almacena la raiz para poder moverla en una variable temporal y no perder la sucesion
		if self.Null() == True: ## Se verifica que contenga datos
			print("\n\tNo hay datos registrados...") ## Si no tiene regresa un mensaje 
		else:
			while temp != None: ## Mientras la variable temporal se diferente a nulo se ejecutara
				print("\t[" + str(temp.dato)+"] ") ## Imprime los datos 
				temp = temp.sig ## Hace que la variable recorra las diferentes posiciones
	
	def Buscar(self,item): ## Funcion que recibe un parametro y lo busca entre los datos almacenados
		temp = self.finT = self.raiz ## Variable que regresa la variable finT a la raiz y la almacena
		i = False ## Variable que controla si existe el dato o no
		while temp != None:  ## Mientras la variable temporal se diferente a nulo se ejecutara
			if temp.dato == item:  ## Verifica si el parametro coincide con algun dato
				i = True ## SI coincide la variable I torna valor verdadero
				return i ## Regresa el valor
			else:
				temp = temp.sig ## SI no existe el dato avanza una posicion y regresa a comparar
	
class  Menu(): ## Clase que controlara las operaciones y lo que se mostrara en consola
	
	def __init__(self): ## Inicia las variables que se usaran
		self.opc = None
		
	def capturar(self): ## Funcion que muestra datos en pantalla y pide los datos
		captura = Operaciones() ## hace referencia a la clase que contiene las operaciones para poder ser usadas
		while True: ## Se crea un ciclo while siempre en verdadero para que se ejecute infinitamente
			print("\n0.-Guardar datos\n1.-Mostrar datos\n2.-Buscar dato\n6.-Salir")
			self.opc = int(input("\n\tIngrese opcion -> ")) ## Se imprimen las operaciones y se captura una opcion
			os.system("clear") ## Limpia la pantalla
			
			if self.opc == 0:
				x = int(input("\n\tIngresa dato: ")) ## pide un dato y lo manda como parametro para ser almacenado
				captura.Ingresar(x)
			
			elif self.opc == 1:
				captura.Recorrer() ## Ejecuta la operacion que muestra todos los datos	
			
			elif self.opc == 2:
				date = int(input("\n\tIngresa dato a buscar: "))
				verificar = captura.Buscar(date) ## Ejecuta la operacion que muestra si un dato existe o no
				if verificar == True: ## Si la funcion regresa un verdadero imprime un mensaje que indica que existe el dato de igual manera si no existe
					print("\n\tDato existente") 
				else:
					print("\n\tNo existe dato")
					
			elif self.opc == 6:
				exit() ## Se sale del programa
				
			else: ## Si ingresa una opcion que no se encuentra en el menu ejecuta un mensaje que indica que es una opcion invalida
				print("\n\tOpcion invalida")


Imprimir = Menu() ## Hace referencia a la clase que contiene el menu para poder ser llamado
Imprimir.capturar() ## Imprime el menu
