#include <bits/stdc++.h>

using namespace std;

int n, k;
int result = 0;

int main() {
    cin >> n >> k;

    while (n > 1) {
        if (n % k == 0) {
            n /= k;
        } else {
            n -= 1;
        }
        result += 1;
    }

    cout << result;
}