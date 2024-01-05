#include <iostream>
#include<algorithm>
#include <vector>

using namespace std;

int main(void) {
    int s, n;
    cin >> s >> n;

    vector<std::pair<int,int>> x;

    int a,b;

    for(int i=0; i < n; i++) {
        cin >> a >> b;
        x.push_back(make_pair(a, b));
    }
    
    bool won = true;

    sort(begin(x), end(x));

    for(int i=0; i < n; i++) {
        if(s <= x[i].first) {
            won = false;
            break;
        } else {
            s += x[i].second;
        }
    }

    if(won) {
        cout << "YES";
    } else {
        cout << "NO";
    }
}