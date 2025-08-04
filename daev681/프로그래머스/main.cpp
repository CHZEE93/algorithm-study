#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    map<string, vector<pair<int, int>>> genreSongs; // 장르별 (play, index)
    map<string, int> genreTotal; // 장르별 총 재생 수

    // 1. 곡 정보 넣기
    for (int i = 0; i < genres.size(); i++) {
        genreSongs[genres[i]].push_back({plays[i], i});
        genreTotal[genres[i]] += plays[i];
    }

    // 2. 장르별 총 재생 수 기준으로 정렬
    vector<pair<string, int>> genreList(genreTotal.begin(), genreTotal.end());
    sort(genreList.begin(), genreList.end(), [](const auto& a, const auto& b) {
        return a.second > b.second; // 총 재생 수 내림차순
    });

    vector<int> answer;

    // 3. 각 장르별로 상위 2곡 뽑기
    for (const auto& entry : genreList) {
        string genre = entry.first;
        auto& songs = genreSongs[genre];

        // 해당 장르 내에서 재생 수 기준 정렬 (동률 시 index 오름차순)
        sort(songs.begin(), songs.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            if (a.first != b.first) return a.first > b.first;
            return a.second < b.second;
        });

        // 최대 2곡까지 push
        for (int i = 0; i < songs.size() && i < 2; i++) {
            answer.push_back(songs[i].second); // index 저장
        }
    }

    return answer;
}