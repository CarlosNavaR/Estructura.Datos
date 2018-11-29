import random

class MergeSort():
	
	def listaAleatorios(self): ## FUncion que genera nuneros aleatorios
	      lista = [0]  * 50 ## Se declara la lista y se multiplica por la cantidad de elementos que contendra para general el espacio
	      for i in range(50): ## Ciclo que genera los numeros aleatorios
	          lista[i] = random.randint(1,100) ## Numeros que se generaran en un rango del 1 al 100 
	      return lista ## Retorna la lista generada aleatoriamente
	      	
	def operaciones(self,izquierda,derecha): ## Funcion que ordenara los datos
		Ordena = [] ## Arreglo donde se almacenaran los datos 
		while len(izquierda) != 0 and len(derecha) != 0: ## Ciclo que se ejecutara siempre y cuando el tamano de las dos variables recibidas seas diferente a 0
			if izquierda[0] < derecha[0]: ## Compara los datos para poder ser asignados al arreglo donde se almacenan ordenados
				Ordena.append(izquierda[0]) ## Si el de la izq es menor que el de la derecha se ingresa este al arreglo
				izquierda.remove(izquierda[0]) ## Y el dato que se encuenta en izq se elimina
			else: ## De lo contrario
				Ordena.append(derecha[0]) ## Ingresara el dato que se encuentra a la derecha al arreglo que los almacena por orden
				derecha.remove(derecha[0]) ## y a si mismo lo eliminara de la derecha
		
		if len(izquierda) == 0: ## Si en el ciclo se cumple que el tamano de los parametros en este caso izq es igual a 0
			Ordena += derecha ## Agrupa datos 
		else:
			Ordena += izquierda ## Agrupa datos
		return Ordena
	
	def merge(self,lista):
		if len(lista) == 0 or len(lista) == 1: ## Compara que cuando el tamano del arreglo sea 1 o 0 pare para que no se mande a llamar infinitamente
			return lista ## Regresa la lista
		else:
			divide = len(lista)/2 ## Divide el arreglo 
			izquierda = self.merge(lista[:divide]) ## Forma recursiva que hace que se guarde desde el 0 hasta el valor que almacene divide
			derecha = self.merge(lista[divide:])  ## Forma recursiva que hace que almacena los valor desde el valor que tiene divide hasta el final
		return self.operaciones(izquierda,derecha) ## Manda a llamar a la funcion que los ordenara
		
	def imprimir(self):
		lista = self.listaAleatorios() ## Almacena el arreglo
		print("\nLista sin Ordenar\n\n" + str(lista)) ## Imprime el arreglo no ordenado 
		ordenada = self.merge(lista) ## Manda el arreglo no ordenado para ser ordenado
		print("\nLista Ordenada\n\n" + str(ordenada)) ## Imprime el arreglo ordenado

up = MergeSort()
up.imprimir()