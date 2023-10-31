#include <iostream>
using namespace std;

int main (){
    int A[9];
    int i, m, max = 0;
    for(i=0; i<9; i++){
        cin >> A[i];
        if (max<A[i]){
            max = A[i];
            m=i;
        }
    }
    cout << max << '\n' << m+1;
    return 0;
}