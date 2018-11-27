import random

class shell():

	def listaAleatorios(self): ## Funcion que genera nuneros aleatorios
	      lista = [0]  * 50 ## Se declara la lista y se multiplica por la cantidad de elementos que contendra para general el espacio
	      for i in range(50): ## Ciclo que genera los numeros aleatorios
	          lista[i] = random.randint(1,100) ## Numeros que se generaran en un rango del 1 al 100 
	      return lista	## Regresa la lista generada
	
	def Ordenamiento(self,lista):
		dif = len(lista) / 2 ## Establecer el tamano de la cantidad de numeros que hara el sato
		while dif >= 1: ## Permitira la ejecucion siempre y cuando la diferencia entre los datos que analizara no sea nula
			for i in range(dif,len(lista)): ## Recorre los elementos de la lista
				aux = lista[i] ## Guarda el elemento 
				temp = i - dif ## GUarda el indice anterior
				while temp >= 0 and lista[temp] > aux: ##Compara los elementos y ordenara
					lista[temp + dif], lista[temp] = lista[temp], lista[temp + dif] ## Ordenada los elementos de la sublitas y los intercambia donde dif son los lugares
					temp -= dif ## Decrementa los elementos
			dif /= 2 ## Reduce los espacios en los que compara formando las nuevas listas
		return lista
	
	def imprimir(self):
		lis = self.listaAleatorios() ## Almacena el arreglo con los datos aleatorios
		print("\nLista sin Ordenar\n\n" + str(lis)) ## Imprime la lista sin ordenar
		self.Ordenamiento(lis) ## Manda los datos para ser ordenados
		print("\nLista Ordenada\n\n" + str(lis)) ## Imprime la lista de manera ordenada
	
up = shell() ##Se asigna la clase a una variable para poder usar sus funciones
up.imprimir()


					
				
			
