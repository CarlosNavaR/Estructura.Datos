/*
	Menu que contiene las praticas 1-2-3
	menu that contains the practices 1-2-3
*/

#include <iostream>
using namespace std;

int menu(){ //Funcion que imprime el menu
	cout<<"Practicas 1-3"<<endl;
	cout<<"Seleccione una opcion\n#1- Primeros 100 numeros naturales\n#2- Factorial por modo de iteracion y modo recursivo\n#3- Metodo Fibonacci con modo de iteracion y modo recursivo\n#4 Salir\n:";
	char a; //Se declara una variable para controlar el menu
	cin>>a; //Lee el dato que se captura
	cout<<endl;
	return a;
}

//Practica #1

int Numero(int x) //Se crea una funcion de tipo entero que recibe un parametro de tipo entero 
{	cout<<x<<endl; //Se imprime la variable recibida como parametro
	if (x<100) //Se declara un condicional para controlar la variable y se defina el tope de rango
	{
		return Numero(x+1); //Se incrementa la variable 
	}
}

void impr() //Funcion que manda el parametro
{
	
	Numero(1); //Se manda a llamar la funcion numero y se le envia el numero 1 como parametro para que sea donde comienza el numero
}

//Practica #2

unsigned long int factorialRecursivo(int n1) //Se declara una funcion y recibe un parametro 
{
   if(n1 == 1) //se compara la variable con 1 para que si es igual regrese el mismo numero, ya que el factorial de 1 es 1 
      {return 1;}
   else
      {return n1*factorialRecursivo(n1-1);} //Se retorna el numero multiplicado por la misma funcion para que se torne de manera recursiva
}

unsigned int FactorialIterativo(int n) //se declara la funcion para trabajar el modo iterativo
{
	int fac=1; // se crea una variable que nos servira como acumulador
	for (int i = 1; i <= n; i++)
	{ 
		fac *= i; //la variable es usada como acumulador y multiplicada por el numero que obtenga del ciclo 
		
	}
	return fac; //regresa los datos acumulados en la variable
}
void practica2() //se declara una funcion para enviar los parametros para usar las funciones con operaciones
{   //Recursive Mode
	int n1; //se declara la variable que es enviada como parametro
	long int result;	//se declara una variable que almacenara lo que retorna la funcion
	
    cout<<"Usando modo recursivo"<<endl;
	cout<<"Ingresa numero para sacar su factorial: ";cin>>n1;
	result=factorialRecursivo(n1); // Se almacena el resultado y al mismo tiempo se llama la funcion para enviar el dato como parametro
	cout<<"Factorial R:"<<result<<"\n\n";
	
	//Interative mode
	int n;  //se declara la variable que es enviada como parametro
	int res; 	//se declara una variable que almacenara lo que retorna la funcion
	
	cout<<"Usando modo iterativo"<<endl;
	cout<<"Ingresa numero para sacar su factorial: ";cin>>n;
	res=FactorialIterativo(n); // Se almacena el resultado y al mismo tiempo se llama la funcion para enviar el dato como parametro
	cout<<"Factorial I:"<<res<<"\n\n";
	
}

//Practica #3


int fibonacciRecursivo(int n) //Modo Recursivo; Se declara una funcion de tipo entero y al mismo tiempo recibe un parametro de tipo entero
{
	if(n<2) //EL dato recibido es puesto en un condicional para comparar que sea menor que 2
		return n; //Si es menor que 2 se regresa el mismo valor
	else
		return fibonacciRecursivo(n-1)+fibonacciRecursivo(n-2); //llama la funcion asi misma para hacer una suma
}
void leerRecursivo(){	//Modo Recursivo 
	int n=0; //se declara una variable que sera usada para enviara como parametro a la funcion fibonacciRecursivo
	cout<<"Ingrese numero para comenzar:\t"; cin>>n;
	for (int i = 1; i <= n; i++) //ciclo que es usado para imprimir los datos del metodo
	{
		cout<<fibonacciRecursivo(i)<<endl; 
	}	
	cout<<"Termina Modo Recursivo"<<endl;
}

int FibonacciIterativo(int n1) //Modo Iterativo; Se declara una funcion de tipo entero y al mismo tiempo recibe un parametro de tipo entero
{
	int i = 0; //Variable que se usara para controlar los valores
	int j = 1;//Variable que se usara para controlar los valores y retornara el resultado
	
	for (int k = 0; k < n1; k++) //CIclo que controlara el rango de 0 a n1 donde las variables locales controlaran los valores
	{	
		int t; //Se declara para almacenar los datos 
		t = i + j; 
		i = j;
		j = t;
	}

	return j;
	
}

void LeerIterativo() //Funcion usada para controlar los parametros que se enviaran a la funcion FibonacciIterativo y su impresion de esta misma
{
	int n1=0;
	cout<<"Ingrese numero para comenzar:\t"; cin>>n1;
	FibonacciIterativo(n1);
	
	for (int i = 0; i < n1; i++) //Ciclo que controla la impresion de los datos que se trabajaro
	{
		cout<<FibonacciIterativo(i)<<endl;
	}	
	
}

void practica3() //Funcion que imprime los datos de FibonacciIterativo y FibonacciRecursivo 
{
	leerRecursivo();	
	LeerIterativo();
	
	
}


int main() //Principal
{
	
	
	switch(menu()) //Ciclo que controla la funcion donde estan los datos del programa
	{
		case '1':
				impr();
				cout<<endl;
				main(); //Al finalizar el programa vuelve a llamarse a la funcion main para hacerse de modo recursiva
			break;
		case '2':
				practica2();
				cout<<endl;
				main();
			break;
		case '3':
				practica3();
				cout<<endl;
				main();
			break;
		case '4':
			exit;
			break;
		default:
			cout<<"\nopcion incorrecta";
			main();
			break;
	}
	
	return 0;
}