/*
	Nava Reyes Carlos - 17212163
	Calcular fibonacci -  Modo iterativo y Recursivo
	Calculate Fibonacci- Interative mode and recursive
	
	En base a la formula  x=(n-1)+(n-1) para el modo recursivo
	Based on the formula  x=(n-1)+(n-1) for the recursive mode

*/

#include <iostream>
using namespace std;

int fibonacciRecursivo(int n) //Modo Recursivo
{
	if(n<2)
		return n;
	else
		return fibonacciRecursivo(n-1)+fibonacciRecursivo(n-2);
}
void leerRecursivo(){	//Modo Recursivo.
	int n=0;
	cout<<"Ingrese numero para comenzar[Recursivo]:\t"; cin>>n;
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
	cout<<"Ingrese numero para comenzar[Iterativo]:\t"; cin>>n1;
	FibonacciIterativo(n1);
	
	for (int i = 0; i < n1; i++)
	{
		cout<<FibonacciIterativo(i)<<endl;
	}	
	
}
int main()
{
	leerRecursivo();	
	LeerIterativo();
	
	return 0;
}