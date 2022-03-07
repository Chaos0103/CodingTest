#include <bits/stdc++.h>

using namespace std;

string str;
vector<char> data;

int main() {
    cin >> str;
    int num = 0;

    for (int i = 0; i < str.size(); i++) {
        if ('A' <= str[i] && str[i] <= 'Z') {
            data.push_back(str[i]);
        } else {
            num += str[i] - '0';
        }
    }

    sort(data.begin(), data.end());

    for (int i = 0; i < data.size(); i++) {
        cout << data[i];
    }
    cout << num << endl;
}
