#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    int d[k];
    for(int i=0; i < k; i++){
        cin >> d[i];
    }
    bool con;

    do {
        con = false;
        for (auto x : d) {
            string number = to_string(n);
            bool found = number.find(to_string(x)) != string::npos;
            if (found) {
                con = true;
                n += 1;
                break;
            }
        }
    } while (con);
    
    cout << n;
    return 0;
}