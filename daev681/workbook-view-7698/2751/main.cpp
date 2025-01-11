#include <iostream>
#include <vector>
#include <algorithm>  
#include <set>
using namespace std;



int main() {
    int  n , m;
    std::cin >> n;
    set<int> s;

    while (n--) {
        int k;
        std::cin >> k;
        s.insert(k);
    }

    
   
    for (const auto& element : s) {
        cout << element << "\n";
    }


    return 0;
}
