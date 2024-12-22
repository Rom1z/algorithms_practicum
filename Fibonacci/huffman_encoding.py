from collections import Counter
import heapq

class Node:
    """Класс для узла дерева Хаффмана"""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    """Строит дерево Хаффмана"""
    freq = Counter(text)
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def build_codes(node, prefix="", code_map=None):
    """Создает коды для символов на основе дерева"""
    if code_map is None:
        code_map = {}
    if node is not None:
        if node.char is not None:
            code_map[node.char] = prefix
        build_codes(node.left, prefix + "0", code_map)
        build_codes(node.right, prefix + "1", code_map)
    return code_map


def huffman_encode(text):
    """Кодирование строк по алгоритму Хаффмана"""
    if not text:
        return "", {}

    # Построение дерева Хаффмана
    root = build_huffman_tree(text)

    # Создание кодов символов
    codes = build_codes(root)

    # Кодирование строки
    encoded_text = "".join(codes[char] for char in text)

    # Вывод результатов
    print(len(codes), len(encoded_text))
    for char, code in sorted(codes.items()):
        print(f"'{char}': {code}")
    print(encoded_text)

    return encoded_text, codes


if __name__ == "__main__":
    text = "Errare humanum est."
    huffman_encode(text)
