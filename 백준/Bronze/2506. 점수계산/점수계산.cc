#include <iostream>
using namespace std;

int main(){
    int n, score=0, res[100], bonus=0;
    cin >> n;
    
    for(int i=1;i<n+1;i++){
        cin >> res[i];
        if(res[i]==1){
            score++;
            if(res[i-1]==1){
                bonus++;
                score += bonus;
            } else {
                bonus=0;
            }
        }
    }
    cout << score;
    return 0;
}