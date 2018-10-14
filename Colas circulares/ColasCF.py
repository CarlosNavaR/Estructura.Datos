import os ## Libreria que permite usar la sentencia os.system("clear")
front = 0 ## Frente de la cola
rear = 0  ## Final de la cola
index = 0 ## Variable que controla el numero de datos ingresados

class ColasC():
	
	def __init__(self):
		self.cola = [0,0,0,0,0] ## Crea e inicializa el arreglo/Lista que almacena los datos
		
	def push(self,item): ## Funcion que ingresa los datos a el arreglo; recibe como parametro un dato
		global front  ##
		global rear   ## Se manda a llamar las variables globales
		global index  ##
		if index == 5: ## Se compara que la variable index no sea igual a 5
			print("\tCola llena") ## Si es igual a 5 quiere decir que esta llena e imprime en mensaje
		else: ## De lo contrario se meten los datos 
			rear = (front + index) % 5 ## Formula que busca la posicion donde se ingresaran los datos y la almacena en una variable
			self.cola[rear] = item ## Se ingresa el dato en la posicion que nos genero la formula
			index += 1 ## EL index se incrementa en 1 
			print("\tFront: " + str(front)) ## Muestra el frente de la cola
			print("\tRear: "+ str(rear))  ## Muestra el final de la cola
			
	def pop(self):	## Funcion encargada de eliminar datos 
		global front ## Se manda a llamar las variables globales
		global index ##
		if index != 0: ## Se condiciona la variable index que sea diferente a 0
			print("\n\tElemento eliminado [" + str(self.cola[front]) +"]") ## Imprime el numero que sera eliminado
			self.cola[front] = 0 ## Se sobrescribe el dato que se encuentra en el frente por vacio o 0 
			front= (front + 1) % 5 ## Formula para calcular la siguiente posicion y a donde se movera el front
			print("\tFront: " + str(front)) ##Se imprime la nueva posicion del front
			index -= 1 ## A la variable index se decrementa en 1 
		else: ## SI la variable index es igual a 0 imprime un mensaje
			print("\n\tIngrese datos, Cola vacia")
	
	def peekfirst(self): ## Funcion que muestra el primer elemento ingresado
		if index!=0: ## Se compara que el index sea diferente a 0 que indica que tiene elementos y puede imprimir el primer elemento ingresado
			print("\n\tProximo dato a salir [" + str(self.cola[front]) + "]")
		else: ## De lo contrario imprime un mensaje en pantalla
			print("\n\tNo hay dato proximo a salir, ingresa datos")	
			
	def Peeklast(self): ## Muestra el ultimo elemento que fue ingresado
		if index!=0: ## Se compara que el index sea diferente a 0 que indica que tiene elementos y puede imprimir el primer elemento ingresado
			print("\n\tUltimo dato a salir [" + str(self.cola[rear]) + "]")
		else: ## De lo contrario imprime un mensaje en pantalla
			print("\n\tRegistre datos; Cola vacia")	
			
	def peekindex(self,item): ## Funcion que busca el indice de cualquier dato que el usuario desee buscar
		z=-1 ## Se declara una variable local para almacenar el index
		for i in range(0,len(self.cola)): ## Se declara un ciclo que recorre la cola 
			if self.cola[i] == item: ## Se comparan todos los datos almacenados con el dato que ingrese el usuario
				z=i ## Se le asigna el indice donde se encuentre el dato
		return z

	def  peekall(self): ## Funcion que imprime toda la cola
		print("")
		for i,j in enumerate(self.cola): ## Ciclo que recorre toda la cola ordenando con su respectivo indice y dato
			print('\t\t\t'+str([i,j])) ## Imprime los datos que se encuentran en la lista	

def menu(): 	## Funcion que controla todo lo que se mirara en pantalla
	colac = ColasC() ## Se declara la clase para poder ser usada
	
	while True: ## Ciclo que siempre esta activo para poder ejecutar el menu las veces que deseen
		
		## Datos que se muestran en pantalla correspondientes al menu
		print("\n\tManejo de colas circulares con sus operaciones basicas ")
		print("\n1.-Push \n2.-Pop \n3.-PeekFirst \n4.-Peeklast \n5.-Peekall \n6.-peekIndex \n7.-Salir")
		opc = int(input("\n\tIngresa opcion\t-> "))
		os.system("clear")## Limpia la pantalla
		
		if opc==1: ## si es igual a 1 ejecuta la funcion push
			print(index)
			x=int(input("\n\tIngresa dato para almacenar -> ")) ## Pide el dato que sera enviado a la funcion push
			print("")
			colac.push(x)
			
		elif opc == 2: ## si es igual 2 elimina un dato
			colac.pop()
		
		elif opc == 3: ## Muestra el primer elemento ingresado
			colac.peekfirst()
		
		elif opc == 4: ## Muestra el ultimo elemento ingresado
			colac.Peeklast()
		
		elif opc == 5: ## Muestra toda la cola
			colac.peekall()
		
		elif opc==6: ## Pide al usuario un dato para buscarlo entre los que estan almacenados
			dato= int(input("\n\tIngresa dato a buscar -> "))
			p = cola.peekindex(dato) ## Almacena el dato que regresa la funcion en una variable local
			if p != -1: ## Se compara que el valor que regreso la funcion sea diferente a -1
				print('\n\tDato [' + str(dato) +'] En posicion [' + str(p) + ']') ## Si fue diferente a -1 imprime el dato y su posicion
			else:
				print("\n\tNo existe dato") ## De lo contrario imprime un mensaje
		
		elif opc==7: ## Se sale del menu
			exit() ## Sentencia que cierra el programa
			
		else : ## SI ingresa una opcion diferente a las que se muestran en pantalla
			print("\nOpcion invalida") ## Se imprime un mensaje de error
			
menu() ## Manda a llamar la funcion que imprime los datos en pantalla
	
		