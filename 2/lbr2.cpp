#include <iostream>
#include <vector>
#include <queue>
#include <deque>
using namespace std;

int main() {
    // Мультисписок
    vector<vector<int>> multiList = {
        {1, 2, 3},
        {4, 5},
        {6, 7, 8}
    };

    // Очередь
    queue<int> q;

    // Дек (двусторонняя очередь)
    deque<int> d;

    // Приоритетная очередь
    priority_queue<int> pq;

    return 0;
}

