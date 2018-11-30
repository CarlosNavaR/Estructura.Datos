import random ## Importa libreria para hacer uso de randint
from time import time ## Importa libreria para medir el tiempo de ejecucion
import sys ## Importa libreria para modificar el numero de recursiones
sys.setrecursionlimit(10000) ## Define como 10 mil el minimo de veces que una funcion puede llamarse a si misma 
class Metodos():
	
	##########################
	#		  Genera 		 #
	#		  Array 		 #
	##########################
	
	def listaAleatorios(self): ## Funcion que genera nuneros aleatorios
	      lista = [0]  * 5000 ## Se declara la lista y se multiplica por la cantidad de elementos que contendra para general el espacio
	      for i in range(5000): ## Ciclo que genera los numeros aleatorios
	          lista[i] = random.randint(1,100) ## Numeros que se generaran en un rango del 1 al 100 
	      return lista ## Retorna la lista generada aleatoriamente
	
	## --->>  	Terminar generar arreglo 	<<--- ###
	
	
	###########################
	#         Metodo          #
	#         Bubble	      #
	###########################
	
	def Bubble(self,lista):  ## Funcion que hara las respectivas comparaciones
		for i in range(1,len(lista)): ## Ciclo que recorrera el arreglo/lista
			for j in range(0,len(lista)-i): 
				if lista[j] > lista[j+1]: ## Condicional que compara los datos
					aux = lista[j] ## si el dato cumple la condicion lo almacena
					lista[j] = lista[j+1] # hace que el dato mayor cambie de posicion
					lista[j+1] = aux # Asigna el valor guardado 
	
	## --->> 	Termina Bubble 		<<---- ###				
	
	##########################
	#		  Metodo  		 #
	#	      Shell			 #
	##########################
	
	def Shell(self,lista):
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
	
	## --->> 	Termina Shell  		<<--- ### 
	
	########################
	#		  Metodo	   #
	#		  Quick		   #
	########################
	
	def dividir(self,lista,menor,mayor): ## Funcion que dividira el arreglo para compararlo
		aux = (menor -1) ## Al macena el dato anterior del puntero menor
		pivote = lista[mayor] ## Asigna el pivote el dato que se encuentra en el puntero mayor
		for i in range(menor,mayor): ## Ciclo que comienza desde el menor hasta el dato mayor
			if lista[i] <= pivote: ## Compara que el dato sea menor o igual que el pivote
				aux += 1 ## Si se cumple la condicion incrementa en uno 
				lista[aux],lista[i] = lista[i],lista[aux] ## Intercambia los valores para dejarlos en orden
		lista[aux+1],lista[mayor] = lista[mayor],lista[aux + 1] ## Si dentro del for no se cumple la condicion intercambia el dato mayor
		return aux+1 ## Regresa el dato de la variable aux aumentada en una para comparar el siguiente dato 
	
	def Quick(self,lista,menor,mayor): ## Funcion que ordenara los datos 
		if menor < mayor: #Verifica que los datos ingresados sean menores para ordenar
			pivot = self.dividir(lista,menor,mayor) ## Crea el pivote para poder compararlos
			self.Quick(lista,menor,pivot - 1) ## Ordena la parte izquiera del pivote
			self.Quick(lista,pivot + 1, mayor) ## Ordena la parte derecha del pivote
	
	def imprimir(self,lista): ## Funcion que imprimira los datos en pantalla
		menor = 0 ## Se le asigna el dato 0 
		lis =lista 
		mayor = len(lis)- 1 ## Asigna el valor en base al tamano del arreglo
		self.Quick(lis,menor,mayor) ## Manda los datos para ser ordenados
		
		
	## --->> 		Termina Quick	 <<--- ###
	
	#######################
	#		 Metodo   	  #
	#		 Merge		  #
	#######################
	
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
	
	## --->> 	Termina Merge  	  <<--- ##


up = Metodos()
lista = up.listaAleatorios()
ShellAr = QuickAr = MergeAr = lista


#print("\n - Datos a ordenar - \n\n" + str(lista) + "\n")

##---> Merge Sort <---##
print("\n--> Merge sort <--\n") ## Imprime el nombre del algoritmo que esta corriendo
start = time() ## Almacena el tiempo de inicio 
up.merge(MergeAr) ## Manda a llamar el algoritmo que ordenara los datos
end = time() ## Almacena el tiempo con el que finalizo el algoritmo
total = end - start ## Con una resta se saca el tiempo total de ejecucion
print("Tiempo de ejecucion " + str(total) + " Segundos\n") ## Imprime en pantalla el tiempo de ejecucion

##---> Termina Merge <---##

##---> Quick Sort <---##
print("--> Quick sort <--\n")
start = time()
up.imprimir(QuickAr)
end = time()
total = end - start
#print(QuickAr)
print("Tiempo de ejecucion " + str(total) + " Segundos\n")
##---> Termina Quick <---##

##---> Shell sort <---##
print("--> Shell sort <--\n")
start = time()
up.Shell(ShellAr)
end = time()
total = end - start
#print(ShellAr)
print("Tiempo de ejecucion " + str(total) + " Segundos\n")

##---> Termina Shell <---##

## ---> Bubble sort <--- ##

print("--> Bubble Sort <--\n")
start = time()
up.Bubble(lista)
end = time()
total = end - start
#print(lista)
print("Tiempo de ejecucion " + str(total) + " Segundos\n")

##  ---> Termina Bubble <--- ##




