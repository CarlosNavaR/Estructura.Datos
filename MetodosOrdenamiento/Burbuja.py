import random ## Libreria que permite usar la funcion randint

class Bubble(): ## Clase que contendra las operaciones para implementar el metodo burbuja
	
	def listaAleatorios(self): ## FUncion que genera nuneros aleatorios
	      lista = [0]  * 50 ## Se declara la lista y se multiplica por la cantidad de elementos que contendra para general el espacio
	      for i in range(50): ## Ciclo que genera los numeros aleatorios
	          lista[i] = random.randint(1,100) ## Numeros que se generaran en un rango del 1 al 100 
	      return lista ## Retorna la lista generada aleatoriamente
	      	
	def Bubble(self,lista):  ## Funcion que hara las respectivas comparaciones
		for i in range(1,len(lista)): ## Ciclo que recorrera el arreglo/lista
			for j in range(0,len(lista)-i): 
				if lista[j] > lista[j+1]: ## Condicional que compara los datos
					aux = lista[j] ## si el dato cumple la condicion lo almacena
					lista[j] = lista[j+1] # hace que el dato mayor cambie de posicion
					lista[j+1] = aux # Asigna el valor guardado 
					
	def Imprimir(self): ## Funcion que mandara a traer las funciones con operaciones y mostrarlas
		print("\n\tMetodo de ordenamiento [bubble sort]")
		lista = self.listaAleatorios() ## Almacena el arreglo
		print("\nLista sin Ordenar\n\n" + str(lista)) ## Imprime el arreglo no ordenado 
		self.Bubble(lista) ## Manda el arreglo no ordenado para ser ordenado
		print("\nLista Ordenada\n\n" + str(lista)) ## Imprime el arreglo ordenado
			
		
up = Bubble() 
up.Imprimir()
  

  
 
