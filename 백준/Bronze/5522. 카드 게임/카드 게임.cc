#include <iostream>
using namespace std;

int main(){
    int num, i, sum=0;
    for(i=0;i<5;i++){
        cin >> num;
        sum += num;
    }
    cout << sum;
    return 0;
}