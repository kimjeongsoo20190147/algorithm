#include <iostream>
using namespace std;

int main() {
    int k,d,a;
    char slash1, slash2;
    cin >> k >> slash1 >> d >> slash2 >> a;
    if(d==0 || k+a<d){
        cout << "hasu";
    }
    else {
        cout << "gosu";
    }
    return 0;
}