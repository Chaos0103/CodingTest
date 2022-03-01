#include <bits/stdc++.h>

using namespace std;

char xPos, yPos;
int result;
int dx[8] = {2, 2, 1, 1, -2, -2, -1, -1};
int dy[8] = {1, -1, 2, -2, 1, -1, 2, -2};

int main() {
    cin >> xPos >> yPos;

    int x = xPos - 'a' + 1;
    int y = yPos - '0';

    for (int i = 0; i < 8; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (1<= nx && nx <= 8 && 1<= ny && ny <= 8) {
            result += 1;
        }
    }
    cout << result << '\n';
    return 0;
}
