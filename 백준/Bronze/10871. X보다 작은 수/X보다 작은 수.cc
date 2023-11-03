#include <iostream>
using namespace std;

int main(){
    int n, x;
    cin >> n >> x;
    
    int A[n];
    
    for(int i=0; i<n; i++){
        cin >> A[i];
        if (A[i]<x){
            cout << A[i] << " ";
        }
    }
}