#include <iostream>
#include <string>
using namespace std;

int main(void) {
    string s;
    string message = "NO";

    if(s=="hello") {
        message = "YES";
    }

    char hello[5] = {'h', 'e', 'l', 'l', 'o'};
    cin >> s;

    string output = "";
    int helloPos = 0;

    for (int i=0; i < s.length(); ++i) {
        if(s[i] == hello[helloPos]) {
            output += s[i];
            helloPos += 1; 
        }

        if(output == "hello") {
            message = "YES";
            break;
        }
    }

    cout << message;
}