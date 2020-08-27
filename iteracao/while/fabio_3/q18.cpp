#include <string>
#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
  int n;
  cout << "Insira o valor de N: ";
  cin >> n;

  int count = 1; // numerador
  double sum = 0.0;

  while (count < n) {
    sum += (double) count / (count == 1 ? n : n - count);
    count++;
  }

  cout << "Valor de S: " << sum << endl;

  return 0;
}