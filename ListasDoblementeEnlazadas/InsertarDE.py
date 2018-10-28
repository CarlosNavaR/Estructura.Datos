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
			
	def Ingresar(self,dato):
		if self.Null() == True: ## Se verifica si la lista esta vacia
			self.raiz = self.fin = Nodo(dato) ## Si esta vacia se les asigna el dato en la primera posicion
		else:
			temporal = self.fin ## Almacena temporalmente el nodo para ligar los datos
			self.fin = temporal.sig = Nodo(dato) ## Liga los nodos con la siguiente posicion y almacena el dato
			self.fin.ant = temporal ## Liga los nodos con el dato anterior
			
			

class  Menu(): ## Clase que controlara las operaciones y lo que se mostrara en consola
	
	def __init__(self): ## Inicia las variables que se usaran
		self.opc = None
		
	def capturar(self): ## Funcion que muestra datos en pantalla y pide los datos
		captura = Operaciones() ## hace referencia a la clase que contiene las operaciones para poder ser usadas
		while True: ## Se crea un ciclo while siempre en verdadero para que se ejecute infinitamente
			print("\n1.-Almacenar datos\n8.-Salir")
			self.opc = int(input("\n\tIngrese opcion -> ")) ## Se imprimen las operaciones y se captura una opcion
			os.system("clear") ## Limpia la pantalla
			
			if self.opc == 1:
				x = int(input("\n\tIngresa dato: ")) ## pide un dato y lo manda como parametro para ser almacenado
				captura.Ingresar(x)
					
			elif self.opc == 8:
				exit() ## Se sale del programa
				
			else: ## Si ingresa una opcion que no se encuentra en el menu ejecuta un mensaje que indica que es una opcion invalida
				print("\n\tOpcion invalida")


Imprimir = Menu() ## Hace referencia a la clase que contiene el menu para poder ser llamado
Imprimir.capturar() ## Imprime el menu

		
			
		
		