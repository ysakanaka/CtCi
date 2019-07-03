class Node():
    def __init__(self, data, adjacency_list = None):
        self.data = data
        self.adjacency_list = adjacency_list or []
        self.shourtest_path = None

    def add_edge_to(self, node):
        self.adjacency_list += [node]

    def __str__(self):
        return self.data

class Queue():
    def __init__(self):
        self.array = []

    def add(self. item):
        self.array.append(item)

    
