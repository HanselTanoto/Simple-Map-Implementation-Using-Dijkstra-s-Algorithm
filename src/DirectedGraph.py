class DirectedGraph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.nodes = len(matrix)
    
    def add_edge(self, u, v, w):
        self.matrix[u][v] = w
    
    def print_graph(self):
        for i in range(self.nodes):
            for j in range(self.nodes):
                print(self.matrix[i][j], end=' ')
            print()

    def get_neighbors(self, u):
        return [i for i in range(self.nodes) if self.matrix[u][i] != 0]
    
    def get_weight(self, u, v):
        return int(self.matrix[u][v])