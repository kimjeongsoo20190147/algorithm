#include <iostream>
using namespace std;

int main() {
    int a, num;
    cin >> a;
    for(int i=1; i<=a ; i++){
        cin >> num;
        cout << "Pairs for "<< num << ": ";
        
        int count = 0;
        for(int j=1; j<=num/2; j++){
            int n = num-j;
            if(n==j||n <=0){
                break;
            } else {
                if(count++){
                    cout << ", ";
                }
                cout << j << " " << n;
            }
        }
        cout << "\n";
    }
    return 0;
}