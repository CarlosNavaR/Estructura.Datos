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
			self.finT.sig = self.fin.sig = self.raiz ## Unen el ultimo elemento con la raiz para que sea circular
		else:
			temporal = self.fin ## Almacena temporalmente el nodo para ligar los datos
			self.finT = self.fin = temporal.sig = Nodo(dato) ## Liga los nodos con la siguiente posicion y almacena el dato
			self.finT.sig = self.fin.sig = self.raiz ## Unen el ultimo elemento con la raiz para que sea circular
			
	def Recorrer(self): ## Funcion que recorre los nodos e imprime los datos
		temp = self.raiz ## Almacena la raiz para poder moverla en una variable temporal y no perder la sucesion
		i = True
		if self.Null() == True: ## Se verifica que contenga datos
			print("\n\tNo hay datos registrados...") ## Si no tiene regresa un mensaje 
		else:
			while i: ## Mientras la variable temporal se diferente a nulo se ejecutara
				print("\t[" + str(temp.dato)+"] ") ## Imprime los datos 
				if temp == self.fin:
					i = False
				else:
					temp = temp.sig ## Hace que la variable recorra las diferentes posiciones
	
	def Buscar(self,item): ## Funcion que recibe un parametro y lo busca entre los datos almacenados
		self.finT = self.raiz ##  Regresa el puntero a la raiz
		temp = 1 ## VAriable temporal que servira para verificar si existe o no el dato
		
		if self.Null() == True: ## Se verifica que la lista no este vacia
			print("\n\tLista vacia")
		else:
			while self.finT.dato != item and temp == 1: ## Se ejecutara el siguiente siempre y cuando el dato no se encuentre y la variable temporal sea 1
				if self.finT.sig != self.raiz: ## Se ejecuta siempre y cuando sea diferente a nulo
					self.finT = self.finT.sig ## Se recorren todos los dato
				else:
					temp = 0
		
			if temp == 0: ## Si el valor de la variable temporal es 0 es por que no se encuentra el dato
				print("\n\tNo existe dato")
			else:
				print("\n\tDato Existente")
				

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
				captura.Buscar(date) ## Ejecuta la operacion que muestra si un dato existe o no
					
			elif self.opc == 6:
				exit() ## Se sale del programa
				
			else: ## Si ingresa una opcion que no se encuentra en el menu ejecuta un mensaje que indica que es una opcion invalida
				print("\n\tOpcion invalida")


Imprimir = Menu() ## Hace referencia a la clase que contiene el menu para poder ser llamado
Imprimir.capturar() ## Imprime el menu
