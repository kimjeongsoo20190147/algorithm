#include <iostream>
using namespace std;

int main() {
    int A,B,C;
    cin >> A >> B >> C;
    
    if (A <= B && C <= A || B <= A && A <= C) {
		cout << A << endl;
	}
	else if (B <= A && C <= B || B <= C && A <= B) {
		cout << B << endl;
	}
	else {
		cout << C << endl;
	}
}