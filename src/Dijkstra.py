import sys

# CONSTANT
INFTY = float("inf")

# Dijkstra class
class Dijkstra:
    def __init__(self, graph, start, end):
        self.graph = graph                                          # DirectedGraph object
        self.start = graph.nodes_name.index(start)                  # Start node
        self.end = graph.nodes_name.index(end)                      # End node
        self.shortest_dist = [INFTY for i in range(graph.nodes)]    # Shortest distance from start to each node
        self.shortest_dist[self.start] = 0                          # Distance from start node to itself is 0
        self.prev_node = [None for i in range(graph.nodes)]         # Previous node in the shortest path
        self.visited = [False for i in range(graph.nodes)]          # Indicates whether a node has been visited
        self.unvisited = []                                         # Explored nodes that are not visited
        self.unvisited.append(self.start)                                # Start node is added to unvisited list
        self.path = []                                              # Path from start to end node
        self.distance = 0                                           # Distance from start to end node
        self.iterate = 0                                            # Iteration count
        self.step = []                                              # Step Information
        self.solve()                                                # Find the shortest path from start to end node
        
    # Dijkstra's Algorithm
    def solve(self):
        while self.unvisited:
            self.iterate += 1
            u = self.unvisited.pop(0)
            self.visited[u] = True
            for v in self.graph.get_neighbors(u):
                if self.visited[v]:
                    continue
                if self.shortest_dist[v] > self.shortest_dist[u] + self.graph.get_weight(u, v):
                    self.shortest_dist[v] = self.shortest_dist[u] + self.graph.get_weight(u, v)
                    self.prev_node[v] = u
                    self.unvisited.append(v)
            self.step.append(self.shortest_dist[:])
        self.path = self.get_path()
        self.distance = self.shortest_dist[self.end]
    
    # Get path from start to end node
    def get_path(self):
        if (self.prev_node[self.end] == None and self.start != self.end):
            return []
        path = [self.graph.nodes_name[self.end]]
        while path[-1] != self.graph.nodes_name[self.start]:
            path.append(self.graph.nodes_name[self.prev_node[self.graph.nodes_name.index(path[-1])]])
        return path[::-1]
    
    # Get path from start to end node as a string
    def get_path_str(self):
        result = ""
        for i in range(len(self.path)):
            if (i == 0):
                result += str(self.path[i])
            else:
                result += " ==> " + str(self.path[i])
        return result
    
    # Print path from start to end node
    def print_path(self):
        print("Shortest path from", self.graph.nodes_name[self.start], "to", self.graph.nodes_name[self.end], "is:", end=" ")
        print(self.path)
        print("Distance:", self.distance)
    
    # Print step information
    def get_step_info(self, i):
        result = ""
        for j in range(self.graph.nodes):
            if (self.step[i][j] == INFTY):
                result += "   Node " + self.graph.nodes_name[j] + "   :   " + "-" + "\n"
            else:
                result += "   Node " + self.graph.nodes_name[j] + "   :   " + str(self.step[i][j]) + "\n"
        return result