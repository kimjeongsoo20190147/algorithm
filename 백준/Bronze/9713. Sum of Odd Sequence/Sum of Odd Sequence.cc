#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T; 
    
    for(int i=0;i<T;i++){
        int a;
        cin >> a;
        
        int sum=0;
        for(int j=1;j<=a;j+=2){
            sum += j;
        }
        cout << sum << endl;
    }
    
}