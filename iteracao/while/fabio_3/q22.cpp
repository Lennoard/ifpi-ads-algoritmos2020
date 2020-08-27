#include <string>
#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
  int n;
  cout << "Insira o valor de N: ";
  cin >> n;

  int count = 1;
  int num = -1;
  double result = 0.0;

  while (count <= 50) {
    num += 2;

    result += (double) num / count;
    count++;
  }

  cout << "Valor de S: " << result << endl;

  return 0;
}