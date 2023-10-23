#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    for (int i=1; i<10; i++) {
        
        int ans = N * i;
        cout << N <<" * " << i << " = " << ans << endl;
    }
    return 0;
    
}