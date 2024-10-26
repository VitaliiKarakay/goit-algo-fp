import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (x - 1 / 2 ** layer, y - 1)
            add_edges(graph, node.left, pos, x=x - 1 / 2 ** layer, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (x + 1 / 2 ** layer, y - 1)
            add_edges(graph, node.right, pos, x=x + 1 / 2 ** layer, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def generate_colors(n):
    if n <= 1:
        return ['#000000'] if n == 1 else []

    colors = []
    for i in range(n):
        shade = int(255 * (i / (n - 1)))
        color = f'#{shade:02x}{shade:02x}{255 - shade:02x}'
        colors.append(color)
    return colors


def dfs(tree_root):
    stack = [tree_root]
    visited = []
    total_nodes = count_nodes(tree_root)
    colors = generate_colors(total_nodes)
    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.append(node)
            node.color = colors[len(visited) - 1]
            draw_tree(tree_root)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


def bfs(tree_root):
    queue = deque([tree_root])
    visited = []
    total_nodes = count_nodes(tree_root)
    colors = generate_colors(total_nodes)
    while queue:
        node = queue.popleft()
        if node and node not in visited:
            visited.append(node)
            node.color = colors[len(visited) - 1]
            draw_tree(tree_root)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def reset_colors(node, default_color="#000000"):
    if node is not None:
        node.color = default_color
        reset_colors(node.left, default_color)
        reset_colors(node.right, default_color)


# Создание дерева с большим количеством узлов
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.left.left.left = Node(11)
root.left.left.right = Node(12)
root.left.right.left = Node(13)
root.left.right.right = Node(14)
root.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
root.right.right.left = Node(9)
root.right.right.right = Node(2)

# Відображення обходу в глибину
dfs(root)


# Скидання кольорів для обходу в ширину
reset_colors(root)

# Відображення обходу в ширину
bfs(root)
