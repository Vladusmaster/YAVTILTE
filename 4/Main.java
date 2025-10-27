import java.util.*;

// ===== ДЕРЕВО =====
class TreeNode<T> {
    T value;                 // значение узла
    TreeNode<T> left;        // левый потомок
    TreeNode<T> right;       // правый потомок

    TreeNode(T value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

        // ===== ГРАФ =====
        class Graph {
            Map<Integer, List<Integer>> adjList = new HashMap<>(); // список смежности

            void addVertex(int vertex) {
                adjList.putIfAbsent(vertex, new ArrayList<>());
            }

            void addEdge(int src, int dest) {
                adjList.get(src).add(dest);
            }
        }
        void main() {
        }
