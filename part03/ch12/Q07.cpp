#include <bits/stdc++.h>

using namespace std;

string str;

int main() {
    cin >> str;
    int result = 0;
    int mid = str.size() / 2;
    for (int i = 0; i < mid; i++) {
        result += str[i] - '0';
    }
    for (int i = mid; i < str.size(); i++) {
        result -= str[i] - '0';
    }

    if (result == 0) {
        cout << "LUCKY" << endl;
    } else {
        cout << "READY" << endl;
    }
}
