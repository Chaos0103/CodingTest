#include <bits/stdc++.h>

using namespace std;

int n, m;
int x, y, dist;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int turnLeft(int d) {
    d -= 1;
    if (d == -1) {
        return 3;
    }
    return d;
}

int main() {
    int map[50][50];
    int visited[50][50] = {0};

    cin >> n >> m;
    cin >> x >> y >> dist;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int num;
            cin >> num;
            map[i][j] = num;
        }
    }

    int turnTime = 0;
    int result = 1;
    visited[x][y] = 1;
    while (true) {
        dist = turnLeft(dist);
        int nx = x + dx[dist];
        int ny = y + dy[dist];
        if (map[nx][ny] == 0 && visited[nx][ny] == 0) {
            visited[nx][ny] = 1;
            x = nx;
            y = ny;
            result += 1;
            turnTime = 0;
            continue;
        } else {
            turnTime += 1;
        }
        if (turnTime == 4) {
            nx = x - dx[dist];
            ny = y - dy[dist];
            if (map[nx][ny] == 0) {
                x = nx;
                y = ny;
            } else {
                break;
            }
            turnTime = 0;
        }
    }

    cout << result << '\n';
    return 0;
}
