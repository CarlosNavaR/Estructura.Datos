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

	

class  Menu(): ## Clase que controlara las operaciones y lo que se mostrara en consola
	
	def __init__(self): ## Inicia las variables que se usaran
		self.opc = None
		
	def capturar(self): ## Funcion que muestra datos en pantalla y pide los datos
		captura = Operaciones() ## hace referencia a la clase que contiene las operaciones para poder ser usadas
		while True: ## Se crea un ciclo while siempre en verdadero para que se ejecute infinitamente
			print("\n1.-Almacenar datos\n2.-Mostrar datos de inicio a fin\n3.-Mostrar datos de final a inicio\n4.-Buscar elemento\n8.-Salir")
			self.opc = int(input("\n\tIngrese opcion -> ")) ## Se imprimen las operaciones y se captura una opcion
			os.system("clear") ## Limpia la pantalla
			
			if self.opc == 1:
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
					
			elif self.opc == 8:
				exit() ## Se sale del programa
				
			else: ## Si ingresa una opcion que no se encuentra en el menu ejecuta un mensaje que indica que es una opcion invalida
				print("\n\tOpcion invalida")


Imprimir = Menu() ## Hace referencia a la clase que contiene el menu para poder ser llamado
Imprimir.capturar() ## Imprime el menu