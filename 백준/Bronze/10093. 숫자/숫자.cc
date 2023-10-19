#include <iostream>
using namespace std;

int main() {
    long a,b;
    cin >> a >> b;
    
    if(a==b){
        cout << 0;
    }
    else if (a<b){
        cout << b-a-1 << endl;
        for(long i=a+1; i<b; i++){
            cout << i << " ";
        }
    }
    else if (a>b) {
        cout << a-b-1 << endl;
        for (long i=b+1; i<a; i++){
            cout << i << " ";
        }
    }
    return 0;
}