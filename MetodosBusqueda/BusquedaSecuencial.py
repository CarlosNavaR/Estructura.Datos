class Secuencial(object): ## Se crea una clase que tendra las operaciones que se realizaran
	
	def __init__(self):
		self.datos = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16] ## Defino una variable de tipo lista con datos pases para que sobre estos se busque un elemento 
		
	def Busqueda(self,lista,dato): ## Funcion que sera encargara de buscar el elemento 
		cont = 0 ## Almacenara la posicion del elemento
		for i in lista: ## Ciclo que recorrera los datos
			if i == dato: ## condicional que verificara si el dato es igual a n 
				return cont + 1 ## Regresa la posicion
			else: 
				cont += 1 ## pasa al siguiente dato
		return -1 ## Regresa -1 si el dato no se encuentra
		
	def imprimir(self): ## Funcion que imprime en pantalla
			print("\n\tMetodo de busqueda Secuencial")
			ls = self.datos ## Almacena la lista en una variable
			print("\n\t"+str(ls))
			a = int(input("\tIngresa numero a buscar:")) ## Pide y almacena el dato a buscar
			num = self.Busqueda(ls,a) ## Manda los dato a la funcion que recorre la lista
			if num != -1: ## Compara el valor que regresa la funcion
				print("\n\tNumero encontrado en la posicion ["+str(num)+"]") ## Imprime la posicion en que se encuentra el dato
			else:
				print("\n\tNumero no encontrado") ## Si no imprime que el dato no se encuentra
up = Secuencial()
up.imprimir()
		