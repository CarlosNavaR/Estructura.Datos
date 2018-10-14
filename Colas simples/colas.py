import os
index = 0 ## Variable global que sirve como contador
class colas(): ## Se crea una clase que contiene las funcion de las operaciones de las colas
	def __init__(self): ##Se define la lista que usaremos para la cola
		self.cola = [] 
	
	def inicializar(self): ## Se inicializa la lista en 0 para poder ser usada con los 5 elementos
		self.cola = [0,0,0,0,0]
	
	def push(self,item): ##Funcion que recibe un parametro que es el que almacenara datos en la lista
		global index ## Se llama la variable que es global
		self.cola[index] = item ## se almacena el dato que se recibio como paramemtro  
		index+=1 ## Variable que incrementa en 1 cada que se ejecuta la funcion
		
	def pop(self): ## Funcion que elimina los elementos de la cola
		global index ## Se llama a la variable global
		if index!=0: ## Se hace una condicion que la variable global sea diferente a 0 si es el caso es que tiene elementos
			print(str("\n\tElemento: [" + str(self.cola[0])) + "] Fue eliminado") ## Imprime el elemento que sera eliminado
			for i in range(0,4): ## Se hace un ciclo que recorre la cola 
				self.cola[i] = self.cola[i+1] ## Recorre la posicion 
			self.cola[4]=0 ## El espacio 4 se le asigna un 0 
			index -=1 ## La variable decrementa en 1 
		else:	## Si no se cumple la condicion es por que la cola esta vacia y se imprime dicho mensaje
			print("\n\tCola vacia")
	
	def peekfirst(self): ## Funcion que muestra el siguiente elemento a salir
		if index!=0: ## Se pasa la variable global por un condicional para ver que la cola no este vacia
			print("\n\tProximo dato a salir [" + str(self.cola[0]) + "]") ## Imprime el mensaje con el numero a salir
		else:
			print("\n\tNo hay dato proximo a salir") ## Si esta vacia se imprime un mensaje 
	
	def peekLast(self): ## Funcion que imprime el ultimo dato que saldra
		if index!=0: ## Se pasa la variable global por un condicional para ver que la cola no este vacia
			if self.cola[4] != 0: ## Se crean multiples condicionales para verificar cual es el ultimo dato a salir
				print("\n\tUltimo dato a salir [" + str(self.cola[4]) + "]")
			elif self.cola[3] != 0:
				print("\n\tUltimo dato a salir [" + str(self.cola[3]) + "]")
			elif self.cola[2] != 0:
				print("\n\tUltimo dato a salir [" + str(self.cola[2]) + "]")
			elif self.cola[1] != 0:
				print("\n\tUltimo dato a salir [" + str(self.cola[1]) + "]")
			elif self.cola[0] != 0:
				print("\n\tUltimo dato a salir [" + str(self.cola[0]) + "]")
		else:
			print("\n\tNo hay datos, ingrese datos") ## Si la cola esta vacia se imprime un mensaje
		
	
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
			
def menu():	## Funcion que controla todo lo que se mirara en pantalla
	cola = colas();	 ## Se declara la clase para poder ser usada
	while True: ## Ciclo que siempre esta activo para poder ejecutar el menu las veces que deseen 
		
		## Datos que se muestran en pantalla correspondientes al menu
		print("\n\tManejo de colas con sus operaciones basicas ")
		print("\t   ~Crear cola antes de ingresar datos~ ")
		print("\n0.-Crear (Si usa esta opcion con datos podria perderlos) \n1.-Push \n2.-Pop \n3.-PeekFirst \n4.-Peeklast \n5.-Peekall \n6.-peekIndex \n7.-Salir")
		opc = int(input("\n\tIngresa opcion\t-> "))
		os.system("clear") ## Limpia la pantalla
		
		if opc==0: ## Si es igual a 0 se llama la funcion inicializar que es la que crea la cola
			cola.inicializar()
			print("\n  Cola creada e inicializada en 0 mire la opcion 5 para ver estos cambios")	
		
		elif opc==1:
			print(index) ## Se imprime esta variable solo para ver en que posicion se ingresara el dato
			if index <= 4: ## Se compara que la variable indice sea menor a 4 que es la capacidad del arreglo
				x=int(input("\n\tIngresa dato para almacenar -> ")) ## Pide al usuario el dato a almacenar
				print("")
				cola.push(x) ## Se envia el dato para que sea almacenado 
			else:
				print("\n\tCola llena") ## Si la variable index sobrepasa el valor declarado es por que ya no hay campos libres en la lista
				
		elif opc==2: ## Si es igual a 2 elimina el primer elemento ingresado y asi sucesivamente
			cola.pop()
			
		elif opc==3: ## Muestra el proximo elemento a salir
			cola.peekfirst()
	
		elif opc==4: ## Muestra el ultimo elemento a salir
			cola.peekLast()
	
		elif opc==5: ## Muestra toda la cola
			cola.peekall()
			
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