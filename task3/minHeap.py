class MinHeap:
    def __init__(self):
        self.heap = []
        self.pos = {}

    def insert(self, v, dist):
        self.heap.append((dist, v))
        self.pos[v] = len(self.heap) - 1
        self._decrease_key(len(self.heap) - 1)

    def _decrease_key(self, idx):
        while idx > 0 and self.heap[idx][0] < self.heap[(idx - 1) // 2][0]:
            self.pos[self.heap[idx][1]] = (idx - 1) // 2
            self.pos[self.heap[(idx - 1) // 2][1]] = idx
            self.heap[idx], self.heap[(idx - 1) // 2] = self.heap[(idx - 1) // 2], self.heap[idx]
            idx = (idx - 1) // 2

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        last_node = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_node
            self.pos[last_node[1]] = 0
            self._heapify(0)
        return root

    def _heapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != idx:
            self.pos[self.heap[smallest][1]] = idx
            self.pos[self.heap[idx][1]] = smallest
            self.heap[smallest], self.heap[idx] = self.heap[idx], self.heap[smallest]
            self._heapify(smallest)

    def decrease_key(self, v, dist):
        idx = self.pos[v]
        self.heap[idx] = (dist, v)
        self._decrease_key(idx)

    def is_empty(self):
        return len(self.heap) == 0