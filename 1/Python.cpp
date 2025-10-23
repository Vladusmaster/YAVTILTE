#include <iostream>
#include <stack>
using namespace std;

int main() {
    // Массив фиксированного размера
    int arr[5] = {1, 2, 3, 4, 5};
    cout << "Элементы массива: ";
    for (int i = 0; i < 5; i++)
        cout << arr[i] << " ";
    cout << endl;

    // Стек
    stack<int> st;
    st.push(10);
    st.push(20);
    st.push(30);

    cout << "Верхний элемент стека: " << st.top() << endl;
    st.pop();
    cout << "Верхний элемент: " << st.top() << endl;

    return 0;
}
