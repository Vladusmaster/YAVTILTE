import java.util.*;

// ---------- БИНАРНАЯ КУЧА ----------

PriorityQueue<Integer> binaryHeap = new PriorityQueue<>();


        // ---------- БИНОМИАЛЬНАЯ КУЧА ----------
        class BinomialNode<T> {
            T key;                    // значение узла
            int degree;               // степень узла
            BinomialNode<T> parent;   // ссылка на родителя
            BinomialNode<T> child;    // ссылка на первого потомка
            BinomialNode<T> sibling;  // ссылка на следующего брата

            BinomialNode(T value) {
                key = value;
                degree = 0;
                parent = null;
                child = null;
                sibling = null;
            }
        }


        // ---------- КУЧА ФИБОНАЧЧИ ----------
        class FibonacciNode<T> {
            T key;                       // значение узла
            int degree;                  // количество дочерних узлов
            boolean mark;                // флаг потери потомка
            FibonacciNode<T> parent;     // ссылка на родителя
            FibonacciNode<T> child;      // ссылка на потомка
            FibonacciNode<T> left;       // левый сосед
            FibonacciNode<T> right;      // правый сосед

            FibonacciNode(T value) {
                key = value;
                degree = 0;
                mark = false;
                parent = null;
                child = null;
                left = this;
                right = this;
            }
        }


        // ---------- ХЕШ-ТАБЛИЦА ----------
        HashMap<Integer, String> hashTable = new HashMap<>();
        void main() {
        }
