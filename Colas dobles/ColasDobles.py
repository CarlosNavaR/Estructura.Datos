import os ## Libreria que permite usar la sentencia os.system("clear")

class Bicola(object): ## Se crea una clase que contendra las funciones con las respectivas operaciones
	def __init__(self):#0 1 2 3 4 5 6 7 8 9
		self.datos =   [0,0,0,0,0,0,0,0,0,0] ## se crea e inicializa el arreglo en 0
		self.Front = 0 # Se declaran e inicializan los apuntadores
		self.Rear = 0 #

		
	def pushFront(self,item):  ## Funcion que nos permitira ingresar los valores por el frente de la cola
		if self.Front == 5: ## Se condiciona a que cuando el front llegue a 5 sea el maximo esto para igualar ambos lados a 5 y tengan la misma capacidad
			print("\n\ttLimite de 5 elementos por lado")
		else:
			self.Front += 1 ## Se incrementa el valor del puntero front
			self.datos[self.Front] = item ## Se ingresan los datos al arreglo/lista
			print("\n\tDato insertado correctamente")
	
	def pushRear(self,item): ## Funcion que permite ingresar por el final de la cola
		if self.Rear == -5:  ## Funcion que nos permitira ingresar los valores por el frente de la cola
			print("\n\tLimite de 5 elementos por lado")
		else:
			self.Rear -= 1 ## Se decrementa el valor del puntero
			self.datos[self.Rear] = item ## Se ingresan los datos al arreglo/lista
			print("\n\tDato insertado correctamente")
			
	def PopRear(self): ## Funcion que nos permitira eliminar por el final
		if self.Front != self.Rear: ## Siempre y cuando sean diferentes los punteros no permitira eliminar
			self.Rear += 1 ## Como en la funcion de ingresar por este lado decrementa en este caso debe aumentar
			self.datos[self.Rear] = 0 ## Deja el valor como 0 
			aux = self.datos[self.Rear-1] ## Recorre el valor
		else:
			print("\n\tNo hay datos para eliminar")
	
	def PopFront(self):
		if self.Front != self.Rear: ## Siempre y cuando sean diferentes los punteros no permitira eliminar
			self.Front -= 1 ## Le quita un valor al frente
			self.datos[self.Front] = 0 ## Se elimina el valor asignandole 0 ya que lo tomo como null
			aux = self.datos[self.Front+1] ## Avanza el puntero
		else:
			print("\n\tNo hay datos para eliminar")
			
	def  peekall(self): ## Funcion que imprime toda la cola
		print("")
		for i,j in enumerate(self.datos): ## Ciclo que recorre toda la cola ordenando con su respectivo indice y dato
			print('\t\t\t'+str([i,j])) ## Imprime los datos que se encuentran en la lista	
			
	def peekfirst(self): ## Funcion que muestra el primer elemento ingresado
		if self.Front != 0:
			print("\n\tFront [" + str(self.datos[self.Front]) + "]")
		else: ## De lo contrario imprime un mensaje en pantalla
			print("\n\tNo hay dato proximo a salir, ingresa datos")	
			
	def Peeklast(self): ## Muestra el ultimo elemento que fue ingresado
		if self.Rear != 0:
			print("\n\tRear [" + str(self.datos[self.Rear]) + "]")
		else: ## De lo contrario imprime un mensaje en pantalla
			print("\n\tRegistre datos; Cola vacia")	
	
	def peekindex(self,item): ## Funcion que busca el indice de cualquier dato que el usuario desee buscar
		z=-1 ## Se declara una variable local para almacenar el index
		for i in range(0,len(self.datos)): ## Se declara un ciclo que recorre la cola 
			if self.datos[i] == item: ## Se comparan todos los datos almacenados con el dato que ingrese el usuario
				z=i ## Se le asigna el indice donde se encuentre el dato
		return z
	
	def Menu(self): ## Funcion que nos mostrara las opciones que tenemos para realizar
		
		while True: ## Ciclo que siempre esta activo para poder ejecutar el menu las veces que deseen
			print("\n1.-pushRear \n2.-pushFront \n3.-PopRear \n4.-PopFront \n5.-peekall \n6.-PeekFront \n7.-PeekRear \n8.-peekindex \n9.-Salir")
			opc = int(input("\n\tIngresa opcion\t-> "))
			os.system("clear")## Limpia la pantalla
			
			if opc == 1:
				x=int(input("\n\tIngresa dato para almacenar -> ")) ## Pide el dato que sera enviado a la funcion push
				print("")
				self.pushRear(x) ## Ingresa datos por el final
			elif opc == 2:
				x=int(input("\n\tIngresa dato para almacenar -> ")) ## Pide el dato que sera enviado a la funcion push
				print("")
				self.pushFront(x) ## Ingresa datos por el frente
			elif opc == 3:
				self.PopRear() ## ELimina un dato del final
			elif opc == 4:
				self.PopFront() ## ELimina el dato por el fente
			elif opc == 5: ## Muestra toda la cola
				self.peekall()
			elif opc == 6:
				self.peekfirst() ## Muestra el front
			elif opc == 7:
				self.Peeklast() ## Muestra el rear
			elif opc == 8:
				dato= int(input("\n\tIngresa dato a buscar -> "))
				p = self.peekindex(dato) ## Almacena el dato que regresa la funcion en una variable local
				if p != -1: ## Se compara que el valor que regreso la funcion sea diferente a -1
					print('\n\tDato [' + str(dato) +'] En posicion [' + str(p) + ']') ## Si fue diferente a -1 imprime el dato y su posicion
				else:
					print("\n\tNo existe dato") ## De lo contrario imprime un mensaje
								
			elif opc==9: ## Se sale del menu
				exit() ## Sentencia que cierra el programa			
			else : ## SI ingresa una opcion diferente a las que se muestran en pantalla
				print("\nOpcion invalida") ## Se imprime un mensaje de error
			

up = Bicola()
up.Menu()	
		
		
		
		

