class DirectedGraph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.nodes = len(matrix)
    
    # Add a new edge to the graph
    def add_edge(self, u, v, w):
        self.matrix[u][v] = w
    
    # Print the graph in matrix form
    def print_graph(self):
        for i in range(self.nodes):
            for j in range(self.nodes):
                print(self.matrix[i][j], end=' ')
            print()

    # Get neighbors of a node
    def get_neighbors(self, u):
        return [i for i in range(self.nodes) if self.matrix[u][i] != 0]
    
    # Get the weight of an edge
    def get_weight(self, u, v):
        return int(self.matrix[u][v])