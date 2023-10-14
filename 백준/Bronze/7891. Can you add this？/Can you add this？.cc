#include <iostream>
using namespace std;

int main(){
    int a;
    cin >> a;
    
    int i;
    i=0;
    
    for (i=0;i<a;i++){
        int x,y,sum;
        cin >> x >> y;
        sum = x+y;
        cout << sum << endl;
    }
    return 0;
}