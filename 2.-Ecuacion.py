###Realizar un programa que resuelva la siguiente ecuacion - > 2^n

def Ecuacion(n): ##Funcion que recibe como parametro n
	if n==0: ##Se usa un condicional para saber si n es igual a 0 ya que todo exponente a la 0 es 1
		return 1
	else:
		return 2 * Ecuacion (n-1) ##Se multiplica el numero al que se le quiere sacar el exponen por la funcion quitandole 1 para multiplicar el mismo numero por n veces
def Datos(): ##Funcion que imprime en pantalla y captura el dato que sera enviado como parametro
	print("\nResolver [2^n]\n")
	n = int(input("Ingresa la potencia \n-> "))
	print("Resultado -> ",Ecuacion(n))
	
Datos()