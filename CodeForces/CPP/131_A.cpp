#include <iostream>
#include <string>
#include <ctype.h>

using namespace std;

int main(void){
    string word;
    string output = "";

    cin >> word;

    bool change = true;

    for(int i=1; i < word.length(); i++) {
        if(islower(word[i])) {
            change = false;
        }
    }

    if(change) {
        for(int i=0; i < word.length(); i++) {
            if(i == 0) {
                if(isupper(word[i])) {
                    output += tolower(word[i]);
                } else {
                    output += toupper(word[i]);
                }
            } else {
                output += tolower(word[i]);
            }
        }
    } else {
        output = word;
    }

    cout << output;
}