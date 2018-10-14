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
			
def menu(): 	## Funcion que controla todo lo que se mirara en pantalla
	colac = ColasC() ## Se declara la clase para poder ser usada
	
	while True: ## Ciclo que siempre esta activo para poder ejecutar el menu las veces que deseen
		
		## Datos que se muestran en pantalla correspondientes al menu
		print("\n\tManejo de colas circulares con sus operaciones basicas ")
		print("\n1.-Push \n7.-Salir")
		opc = int(input("\n\tIngresa opcion\t-> "))
		os.system("clear")## Limpia la pantalla
		
		if opc==1: ## si es igual a 1 ejecuta la funcion push
			print(index)
			x=int(input("\n\tIngresa dato para almacenar -> ")) ## Pide el dato que sera enviado a la funcion push
			print("")
			colac.push(x)
		
		elif opc==7: ## Se sale del menu
			exit() ## Sentencia que cierra el programa
			
		else : ## SI ingresa una opcion diferente a las que se muestran en pantalla
			print("\nOpcion invalida") ## Se imprime un mensaje de error
			
menu() ## Manda a llamar la funcion que imprime los datos en pantalla
	
		