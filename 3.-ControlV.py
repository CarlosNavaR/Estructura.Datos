## Control de versiones de un proyecto en una empresa
## La estructura debe controlar el numero de migraciones realizadas en el proyecto
## Utilizar una pila para introducir las migraciones una por una
## Obtener las migraciones una por una de la mas reciente a la mas antigua
import os
class ControlV(): ##Se crea una clase que controla la pila y las operaciones

	def __init__(self): 
		self.pila = []
	
	def push(self,item): ##Funcion para ingresar las versiones
			self.pila.append(item)
			
	def peek(self): ##Funcion que muestra todas las versiones del proyecto
			self.pila.reverse()  ##Invierte la pila para mostrar del mas reciente al mas antiguo
			if len(self.pila) == 0: ##Si la lista esta vacia retornar un mensaje
				print("\t\tNo hay versiones disponibles\n\tRegistre versiones para tener la vista previa")
			else:
				print("\t[Dia]-[Mes]-[Anio]")
				for i in self.pila: ## Imprimer la pila
					print("\n\t"+str( i ))				
		
def menu(): ##Funcion que controla el sistema de versiones
	control = ControlV()
	while True:
		print("\n\tBienvenido al control de versiones\n")
		print("1.-Registrar nueva version\n2.-Mostrar versiones\n3.-Salir")
		opc = int(input("Ingresa opcion -> "))
		os.system("clear") 
		if opc==1:
			print("\n\t\tRegistra la migracion con el siguiente formato\n")
			print("\t\t    Formato [dia 01 - mes [1-12] - anio 2019]\n")
			print("\tTomando en cuenta que los registros van del mas antiguo al mas reciente")
			dia = input("\n\t:Ingresa migracion ->\n\t[Dia] ") 
			mes = input("\t[Mes] ") 
			anio = input("\t[Anio] ")
			migracion = dia,mes,anio
			if mes<=12 and mes>0 and anio >= 1000 and anio <=9999:
					control.push(migracion)
					print("\n\tRegistrado correctamente")
			else:
				print("\n\tERROR: Revisa que tus datos esten correctos")
		elif opc==2:
			print("\n\t\tMigraciones:\n")
			control.peek()
		elif opc==3:
			exit()
		else:
			print("\n\t\tOpcion invalida")

menu()