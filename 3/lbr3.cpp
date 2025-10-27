#include <iostream>
#include <queue>
#include <unordered_map>
using namespace std;

// БИНАРНАЯ КУЧА
priority_queue<int, vector<int>, greater<int>> binaryHeap;
// min-heap — элементы с наименьшим значением находятся наверху


// БИНОМИАЛЬНАЯ КУЧА
template <typename T>
struct BinomialNode {
    T key;                       // значение узла
    int degree;                  // степень узла (число дочерних деревьев)
    BinomialNode<T>* parent;     // ссылка на родителя
    BinomialNode<T>* child;      // ссылка на первого потомка
    BinomialNode<T>* sibling;    // ссылка на следующего брата

    // Конструктор
    BinomialNode(T value) {
        key = value;
        degree = 0;
        parent = nullptr;
        child = nullptr;
        sibling = nullptr;
    }
};


// КУЧА ФИБОНАЧЧИ
template <typename T>
struct FibonacciNode {
    T key;                        // значение узла
    int degree;                   // количество дочерних узлов
    bool mark;                    // флаг потери потомка
    FibonacciNode<T>* parent;     // ссылка на родителя
    FibonacciNode<T>* child;      // ссылка на потомка
    FibonacciNode<T>* left;       // левый сосед
    FibonacciNode<T>* right;      // правый сосед

    // Конструктор
    FibonacciNode(T value) {
        key = value;
        degree = 0;
        mark = false;
        parent = nullptr;
        child = nullptr;
        left = this;
        right = this;
    }
};


// ХЕШ-ТАБЛИЦА
unordered_map<int, string> hashTable;
// хранит пары "ключ-значение", обеспечивает быстрый доступ по ключу


int main() {
    return 0;
}
