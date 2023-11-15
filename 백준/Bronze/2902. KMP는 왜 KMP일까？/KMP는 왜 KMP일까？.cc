#include <iostream>
using namespace std;

int main(){
    string input;
    cin >> input;

    cout << input[0];
    
    for (int i = 1; i < input.length(); i++){
        if(input[i] == '-'){
            cout << input[i + 1];
        }
    }

    return 0;
}
