# Бинарная куча (min-heap)
import heapq
binary_heap = []

# Биномиальная куча
class Node:
    def __init__(self, key):
        # Initialize node data,
        # degree, and pointers.
        self.data = key
        self.degree = 0
        self.child = None
        self.parent = None
        self.sibling = None

# Merges two Binomial Trees.

def mergeBinomialTrees(b1, b2):
    # Ensure b1 has smaller value.
    if b1.data > b2.data:
        b1, b2 = b2, b1

    # Make b2 a child of b1.
    b2.parent = b1
    b2.sibling = b1.child
    b1.child = b2
    b1.degree += 1

    return b1

# Куча Фибоначчи (через стороннюю библиотеку)
# pip install fibonacci-heap-mod
from fibonacci_heap_mod import Fibonacci_heap
fib_heap = Fibonacci_heap()

# Хеш-таблица (стандартный словарь Python)
hash_table = {1:"1"}
