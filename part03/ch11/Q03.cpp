#include <bits/stdc++.h>

using namespace std;

string str;

int main() {
    cin >> str;

    int cnt = 1;
    for (int i = 1; i < str.size(); i++) {
        if (str[i - 1] != str[i]) {
            cnt++;
        }
    }

    cout << cnt / 2 << endl;
}
