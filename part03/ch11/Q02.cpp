#include <bits/stdc++.h>

using namespace std;

string data;
int result;

int main() {
    cin >> data;

    for (int i = 0; i < data.size(); i++) {
        int num = data[i] - '0';
        if (result <= 1 or num <= 1) {
            result += num;
        } else {
            result *= num;
        }
    }

    cout << result << endl;
}
