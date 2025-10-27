# дерево
class TreeNode:
    def __init__(self, value):
        self.value = value      # значение узла
        self.left = None        # ссылка на левое поддерево
        self.right = None       # ссылка на правое поддерево


# Граф
class Graph:
    def __init__(self):
        self.adj_list = {}  # словарь: вершина -> список соседей

    def add_vertex(self, vertex):
        self.adj_list[vertex] = []

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
