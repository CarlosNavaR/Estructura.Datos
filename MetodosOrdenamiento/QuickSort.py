import random

class QuickSort(): ## Clase que almacena las operaciones para ordernar por ordenamiento rapido
					
	def listaAleatorios(self): ## Funcion que genera nuneros aleatorios
	      lista = [0]  * 50 ## Se declara la lista y se multiplica por la cantidad de elementos que contendra para general el espacio
	      for i in range(50): ## Ciclo que genera los numeros aleatorios
	          lista[i] = random.randint(1,100) ## Numeros que se generaran en un rango del 1 al 100 
	      return lista	## Regresa la lista generada
	
	def dividir(self,lista,menor,mayor): ## Funcion que dividira el arreglo para compararlo
		aux = (menor -1) ## Al macena el dato anterior del puntero menor
		pivote = lista[mayor] ## Asigna el pivote el dato que se encuentra en el puntero mayor
		for i in range(menor,mayor): ## Ciclo que comienza desde el menor hasta el dato mayor
			if lista[i] <= pivote: ## Compara que el dato sea menor o igual que el pivote
				aux += 1 ## Si se cumple la condicion incrementa en uno 
				lista[aux],lista[i] = lista[i],lista[aux] ## Intercambia los valores para dejarlos en orden
		lista[aux+1],lista[mayor] = lista[mayor],lista[aux + 1] ## Si dentro del for no se cumple la condicion intercambia el dato mayor
		return aux+1 ## Regresa el dato de la variable aux aumentada en una para comparar el siguiente dato 
	
	def Ordenamiento(self,lista,menor,mayor): ## Funcion que ordenara los datos 
		if menor < mayor: #Verifica que los datos ingresados sean menores para ordenar
			pivot = self.dividir(lista,menor,mayor) ## Crea el pivote para poder compararlos
			self.Ordenamiento(lista,menor,pivot - 1) ## Ordena la parte izquiera del pivote
			self.Ordenamiento(lista,pivot + 1, mayor) ## Ordena la parte derecha del pivote
		
	def imprimir(self): ## Funcion que imprimira los datos en pantalla
		menor = 0 ## Se le asigna el dato 0 
		lis = self.listaAleatorios() ## Almacena el arreglo con los datos aleatorios
		mayor = len(lis)- 1 ## Asigna el valor en base al tamano del arreglo
		print("\nLista sin Ordenar\n\n" + str(lis)) ## Imprime la lista sin ordenar
		self.Ordenamiento(lis,menor,mayor) ## Manda los datos para ser ordenados
		print("\nLista Ordenada\n\n" + str(lis)) ## Imprime la lista de manera ordenada
		
up = QuickSort()
up.imprimir()