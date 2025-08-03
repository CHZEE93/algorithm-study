#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main() {
    vector<string> cards(5);
    map<char, int> colorCount;
    map<int, int> numberCount;
    vector<int> numbers;

    for (int i = 0; i < 5; i++) {
        cin >> cards[i];
        char color = cards[i][0];
        int num = cards[i][1] - '0';

        colorCount[color]++;
        numberCount[num]++;
        numbers.push_back(num);
    }

    sort(numbers.begin(), numbers.end());

    // 색이 모두 같으면 true
    bool isFlush = (colorCount.size() == 1);

    // 숫자가 연속이면 true
    bool isStraight = true;
    for (int i = 1; i < 5; i++) {
        if (numbers[i] != numbers[i - 1] + 1) {
            isStraight = false;
            break;
        }
    }

    int maxScore = 0;

    // 1. 같은 색 + 연속 (스트레이트 플러시)
    if (isFlush && isStraight) {
        maxScore = max(maxScore, numbers.back() + 900);
    }

    // 2. Four of a kind
    for (map<int, int>::iterator it = numberCount.begin(); it != numberCount.end(); ++it) {
        int key = it->first;
        int val = it->second;
        if (val == 4) {
            maxScore = max(maxScore, key + 800);
        }
    }

    // 3. Full House
    int three = 0, two = 0;
    for (map<int, int>::iterator it = numberCount.begin(); it != numberCount.end(); ++it) {
        int key = it->first;
        int val = it->second;
        if (val == 3) three = key;
        else if (val == 2) two = max(two, key);  // 큰 숫자가 앞에 오게
    }
    if (three && two) {
        maxScore = max(maxScore, three * 10 + two + 700);
    }

    // 4. Flush
    if (isFlush) {
        maxScore = max(maxScore, numbers.back() + 600);
    }

    // 5. Straight
    if (isStraight) {
        maxScore = max(maxScore, numbers.back() + 500);
    }

    // 6. Three of a kind (단, Full House 아니어야 함)
    for (map<int, int>::iterator it = numberCount.begin(); it != numberCount.end(); ++it) {
        int key = it->first;
        int val = it->second;
        if (val == 3) {
            maxScore = max(maxScore, key + 400);
        }
    }

    // 7. Two Pairs
    vector<int> pairs;
    for (map<int, int>::iterator it = numberCount.begin(); it != numberCount.end(); ++it) {
        if (it->second == 2) {
            pairs.push_back(it->first);
        }
    }
    if (pairs.size() == 2) {
        sort(pairs.begin(), pairs.end());
        maxScore = max(maxScore, pairs[1] * 10 + pairs[0] + 300);
    }

    // 8. One Pair (주의: 위에서 이미 두 쌍 처리한 뒤에 해야 함)
    if (pairs.size() == 1) {
        maxScore = max(maxScore, pairs[0] + 200);
    }

    // 9. 아무것도 아닐 때
    maxScore = max(maxScore, numbers.back() + 100);

    cout << maxScore << endl;
    return 0;
}
