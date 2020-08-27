#include <string>
#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
  int n;
  cout << "Insira o valor de N: ";
  cin >> n;

  int cont = 1;
  double sum = 0.0;

  while (cont < n) {
    sum += 1.0 / cont;
    cont++;
  }

  cout << "Valor de S: " << sum << endl;

  return 0;
}