from pyvis.network import Network


# Draws the graph 
def drawGraph(graph):
    net = Network(height="700px", width="800", bgcolor="#222222", font_color="black", directed=True)
    for i in range(graph.nodes):
        net.add_node(i, label=graph.nodes_name[i], title=str(i), shape="circle", color="#3DFF94", labelHighlightedBold=True)
    for i in range(graph.nodes):
        for j in range(graph.nodes):
            if graph.matrix[i][j] != 0:
                net.add_edge(i, j, weight=graph.matrix[i][j], label=str(graph.matrix[i][j]), color="#00C8FF")
    net.save_graph(r"..\utils\graph.html")


# Draws the graph with the shortest path
def drawPath(graph, dijkstra):
    net = Network(height="700px", width="800", bgcolor="#222222", font_color="black", directed=True)
    for i in range(graph.nodes):
        if (graph.nodes_name[i] in dijkstra.path):
            net.add_node(i, label=graph.nodes_name[i], title=str(i), shape="circle", color="yellow", labelHighlightedBold=True)
        else:
            net.add_node(i, label=graph.nodes_name[i], title=str(i), shape="circle", color="#3DFF94", labelHighlightedBold=True)
    for i in range(graph.nodes):
        for j in range(graph.nodes):
            if graph.matrix[i][j] != 0:
                if (graph.nodes_name[i] + graph.nodes_name[j]) in ("".join(e for e in dijkstra.path)):
                    net.add_edge(i, j, weight=graph.matrix[i][j], label=str(graph.matrix[i][j]), color="red", width=4)
                else:
                    net.add_edge(i, j, weight=graph.matrix[i][j], label=str(graph.matrix[i][j]), color="#00C8FF")
    net.save_graph(r"..\utils\graph.html")