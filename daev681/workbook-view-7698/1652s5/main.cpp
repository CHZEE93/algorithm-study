#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> sv(n);

    // 입력 받기
    for (int i = 0; i < n; i++) {
        cin >> sv[i];
    }

    int row_count = 0, col_count = 0;

    // 가로 자리 계산
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (sv[i][j] == '.') {
                count++;
            } else {
                if (count >= 2) {
                    row_count++;
                }
                count = 0; // Reset
            }
        }
        if (count >= 2) {
            row_count++; // 마지막 연속된 자리 처리
        }
    }

    // 세로 자리 계산
    for (int j = 0; j < n; j++) {
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (sv[i][j] == '.') {
                count++;
            } else {
                if (count >= 2) {
                    col_count++;
                }
                count = 0; // Reset
            }
        }
        if (count >= 2) {
            col_count++; // 마지막 연속된 자리 처리
        }
    }

    // 결과 출력
    cout << row_count << " " << col_count;

    return 0;
}
