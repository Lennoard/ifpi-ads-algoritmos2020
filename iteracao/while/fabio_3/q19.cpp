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
  double result = 0.0;

  while (count < n) {
    if (count % 2 == 1) {
      result -= (double) count / (count == 1 ? n : n - (count - 1));
    } else {
      result += (double) n - (count - 1) / count;
    }
    count++;
  }

  cout << "Valor de S: " << result << endl;

  return 0;
}