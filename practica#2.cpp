/*
Nava Reyes Carlos - 17212163
Calcular factorial dado por usuario y desplegar resultado Modo iteracion y recursivo
calculate factorial, given by user and display result, interative mode and recursive mode
*/

#include <iostream>
using namespace std;

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

int main(void)
{   //Recursive Mode
	int n1; //Numero que se envia al modulo
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
	
	return 0;
}


	
