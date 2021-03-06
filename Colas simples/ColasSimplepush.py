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
		
def menu():	## Funcion que controla todo lo que se mirara en pantalla
	cola = colas();	 ## Se declara la clase para poder ser usada
	while True: ## Ciclo que siempre esta activo para poder ejecutar el menu las veces que deseen 
		
		## Datos que se muestran en pantalla correspondientes al menu
		print("\n\tManejo de colas con sus operaciones basicas ")
		print("\t   ~Crear cola antes de ingresar datos~ ")
		print("\n0.-Crear (Si usa esta opcion con datos podria perderlos) \n1.-Push \n7.-Salir")
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
						
		elif opc==7: ## Se sale del menu
			exit() ## Sentencia que cierra el programa
			
		else : ## SI ingresa una opcion diferente a las que se muestran en pantalla
			print("\nOpcion invalida") ## Se imprime un mensaje de error
			
menu() ## Manda a llamar la funcion que imprime los datos en pantalla