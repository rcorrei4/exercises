#include <iostream>
#include <string>
using namespace std;

int main(void){
    int w, count;
    string output = "NO";
    count = 0;
    cin >> w;

    for(int i=2; i < w; i++){
        if(i % 2 == 0) {
            count += i;

            if ((w-count) % 2 == 0) {
                output = "YES";
            }
        }
    }

    cout << output;
}