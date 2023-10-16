#include <iostream>
using namespace std;

int main(){
    int a, i, sum;
    cin >> a;
    
    i=0;
    sum=0;
    for (i=0; i<a+1 ; i++){
        sum += i;
    }
    
    cout << sum;
    return 0;
}