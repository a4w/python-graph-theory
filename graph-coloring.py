import networkx as nx
import matplotlib.pyplot as plt

def colorGraph(adjList):
    colors = ["#FF0000", "#00FF00", "#0000FF", "#00FFFF"]
    colorList = dict()
    G = nx.MultiGraph()
    # Start graph coloring
    for color in colors:
        for node in adjList:
            if(node in colorList):
                continue
            adjNodes = adjList[node]
            can = True
            for adjNode in adjNodes:
                if(adjNode in colorList and colorList[adjNode] == color):
                    can = False
                    break
            if(can):
                colorList[node] = color
    
    graphColors = []
    # Add nodes to graph
    for node in adjList:
        G.add_node(node)
        graphColors.append(colorList[node])
        for adj in adjList[node]:
            G.add_edge(node, adj)
    nx.draw(G, node_color=graphColors, with_labels=True)
    plt.show()