#include <bits/stdc++.h>

using namespace std;

int n = 1260;
int coins[4] = {500, 100, 50, 10};
int result = 0;

int main() {

    for (int i = 0; i < 4; i++) {
        result += n / coins[i];
        n %= coins[i];
    }

    cout << result << endl;
}
