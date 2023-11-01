#include <iostream>
using namespace std;

int main(){
    int A[7];
    int i, sum = 0;
    int min = 100;
    for(i=0; i<7 ; i++){
        cin >> A[i];
        if(A[i] % 2 == 1){
            sum += A[i];
            if (min > A[i]){
                min = A[i];
            }
        }
    }
    if (sum ==0){
        cout << -1;
    }
    else {
        cout << sum << '\n' << min;
    }
    return 0;
}