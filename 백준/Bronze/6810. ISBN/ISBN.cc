#include <iostream>
using namespace std;

int main(){
    int a,b,c;
    cin >> a >> b >> c;
    
    int sum;
    sum = 91;
    sum += a*1;
    sum += b*3;
    sum += c*1;
    
    cout << "The 1-3-sum is " << sum;
    return 0;
}