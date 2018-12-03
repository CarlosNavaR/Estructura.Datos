class Binaria(object): ## Clase que contendra las funciones para resolver el problema
	
	def __init__(self):
		self.lista = [1,2,3,4,5,6,7,21,13,24,25,28,45,46,50] ## Variable que almacena los datos en la lista
	
	def Busqueda(self,lista,dato): ## Funcion que buscara los datos
		inicio =  0 ## Variable que almacenara el primer dato
		fin = len(lista) -1 ## Variable que almacena el ultimo dato
		while inicio < fin: ## Ciclo que mientras el inicio sea menor al dato final se ejecutara
			pivote = int ((inicio + fin)/2) ## Sacara el dato medio de la lista 
			if lista[pivote] == dato: ## Condicional que verifica si el dato es el pivote 
				return pivote ## Retorna el pivote si es que se encuentra ahi 
			elif lista[pivote] < dato: ## SI no  compara si el dato es menor que el pivote y ejecuta el metodo por el lado izquiero 
				inicio = pivote + 1 ## Aumeneta los datos para ir comparandolos
			else: ## Si no se cumplen las condiciones anteriores se va con el lado derecho
				fin = pivote - 1 ## Se va por el lado derecho decrementando los datos para compararlo 
		return -1 ## Si no se encuentra el dato regresa -1 
	
	def imprimir(self):
		ls = self.lista ## Almacena la lista 
		print("\n\t"+str(ls))
		num = int(input("\n\tIngresa numero a buscar: "))
		item = self.Busqueda(ls,num) ## Manda el dato a buscar a la funcion
		if item != -1:
			print("\n\tNumero encontrado en la posicion ["+str(item+1)+"]") ## Imprime la posicion en que se encuentra el dato
		else:
			print("\n\tNumero no encontrado") ## Si no imprime que el dato no se encuentra
		
up = Binaria()
up.imprimir()
		