#include <iostream>
using namespace std;
#include <limits> 
int main(){

  int n;
  cin >> n;
  int max = numeric_limits<int>::min(); 
  int min = numeric_limits<int>::max(); 

  for (int i = 0; i < n; ++i) { 
    int age;
    cin >> age;

    
    if (age > max) { // 최대값 갱신
        max = age;
    }
    if (age < min) { // 최소값 갱신
        min = age;
    }
   }

   cout << max - min << endl;

}