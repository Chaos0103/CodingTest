#include <bits/stdc++.h>

using namespace std;

int n;
int result;

int main() {
    cin >> n;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j < 60; j++) {
            for (int k = 0; k < 60; k++) {
                if (i == 3 || j / 10 == 3 || j % 10 == 3 || k / 10 == 3 || k % 10 == 3) {
                    result += 1;
                }
            }
        }
    }

    cout << result << '\n';
}
