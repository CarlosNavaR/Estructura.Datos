/*
	Menu que contiene las praticas 1-2-3
	menu that contains the practices 1-2-3
*/

#include <iostream>
using namespace std;

int menu(){
	cout<<"Practicas 1-3"<<endl;
	cout<<"Seleccione una opcion\n#1- Primeros 100 numeros naturales\n#2- Factorial por modo de iteracion y modo recursivo\n#3- Metodo Fibonacci con modo de iteracion y modo recursivo\n#4 Salir\n:";
	char a;
	cin>>a;
	cout<<endl;
	return a;
}

//Practica #1

int Numero(int x)
{	cout<<x<<endl;
	if (x<100)
	{
		return Numero(x+1);
	}
}

void impr()
{
	
	Numero(1);
}

//Practica #2

unsigned long int factorialRecursivo(int n1)
{
   if(n1 == 1)
      {return 1;}
   else
      {return n1*factorialRecursivo(n1-1);}
}

unsigned int FactorialIterativo(int n)
{
	int fac=1;
	for (int i = 1; i <= n; i++)
	{
		fac *= i;
		
	}
	return fac;
}
void practica2()
{   //Recursive Mode
	int n1;
	long int result;
	
    cout<<"Usando modo recursivo"<<endl;
	cout<<"Ingresa numero para sacar su factorial: ";cin>>n1;
	result=factorialRecursivo(n1);
	cout<<"Factorial R:"<<result<<"\n\n";
	
	//Interative mode
	int n;
	int res;
	
	cout<<"Usando modo iterativo"<<endl;
	cout<<"Ingresa numero para sacar su factorial: ";cin>>n;
	res=FactorialIterativo(n);
	cout<<"Factorial I:"<<res<<"\n\n";
	
}

//Practica #3


int fibonacciRecursivo(int n) //Modo Recursivo
{
	if(n<2)
		return n;
	else
		return fibonacciRecursivo(n-1)+fibonacciRecursivo(n-2);
}
void leerRecursivo(){	//Modo Recursivo.
	int n=0;
	cout<<"Ingrese numero para comenzar:\t"; cin>>n;
	for (int i = 1; i <= n; i++)
	{
		cout<<fibonacciRecursivo(i)<<endl;
	}	
	cout<<"Termina Modo Recursivo"<<endl;
}

int FibonacciIterativo(int n1) //Modo Iterativo
{
	int i = 0;
	int j = 1;
	
	for (int k = 0; k < n1; k++)
	{	
		int t;
		t = i + j;
		i = j;
		j = t;
	}

	return j;
	
}

void LeerIterativo()
{
	int n1=0;
	cout<<"Ingrese numero para comenzar:\t"; cin>>n1;
	FibonacciIterativo(n1);
	
	for (int i = 0; i < n1; i++)
	{
		cout<<FibonacciIterativo(i)<<endl;
	}	
	
}

void practica3()
{
	leerRecursivo();	
	LeerIterativo();
	
	
}


int main() //Principal
{
	
	
	switch(menu())
	{
		case '1':
				impr();
				cout<<endl;
				main();
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