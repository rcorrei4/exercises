#include <iostream>
#include <string>
using namespace std;

int main(void){
    string players;
    string output = "NO";

    cin >> players;

    int repeat_count = 1;
    
    for(int i=1; i < players.length(); i++){
        if(players[i-1] == players[i]){
            repeat_count += 1;
        } else {
            repeat_count = 1;
        }

        if(repeat_count >= 7){
            output = "YES";
        }
    }

    cout << output;
}