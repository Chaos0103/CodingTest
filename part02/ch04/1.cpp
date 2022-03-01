#include <bits/stdc++.h>

using namespace std;

int n;
string str;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0,};
char dist[4] = {'L', 'R', 'U', 'D'};
int x = 1, y = 1;

int main() {
    cin >> n;
    cin.ignore();
    getline(cin, str);
    for (int i = 0; i < str.size(); i++) {
        char plan = str[i];
        if (plan == ' ') continue;
        int nx, ny;
        for (int j = 0; j < 4; j++) {
            if (plan == dist[j]) {
                nx = x + dx[j];
                ny = y + dy[j];
                break;
            }
        }
        if (nx < 1 or nx > n or ny < 1 or ny > n) continue;
        x = nx;
        y = ny;
    }

    cout << x << ' ' << y << '\n';
}