#include <iostream>
#include <vector>
#include <map>
using namespace std;

//  ДЕРЕВО
template <typename T>
struct TreeNode {
    T value;           // значение узла
    TreeNode* left;    // левый потомок
    TreeNode* right;   // правый потомок

    // Конструктор
    TreeNode(T val) {
        value = val;
        left = nullptr;
        right = nullptr;
    }
};

// ГРАФ
struct Graph {
    map<int, vector<int>> adjList; // список смежности: вершина -> соседи

    // Добавление вершины
    void addVertex(int vertex) {
        adjList[vertex]; // создаёт пустой список, если вершина новая
    }

    // Добавление ребра
    void addEdge(int src, int dest) {
        adjList[src].push_back(dest);
    }
};

// Проверка компиляции
int main() {
    TreeNode<int> root(10);
    Graph g;
    g.addVertex(1);
    g.addVertex(2);
    g.addEdge(1, 2);
    return 0;
}
