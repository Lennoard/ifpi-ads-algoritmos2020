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
  double result = 0.0;

  while (count < n) {
    if (count % 2 == 1) {
      result -= 1.0 / count;
    } else {
      result += 1.0 / count;
    }
    count++;
  }

  cout << "Valor de S: " << result << endl;

  return 0;
}