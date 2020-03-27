import networkx as nx
import matplotlib.pyplot as plt
from GraphVisualizerGUI import *

def colorGraph(adjList):
    availableColors = ["#FF0000", "#00FF00", "#0000FF", "#00FFFF"]
    colorList = dict()
    G = nx.MultiGraph()
    # Start graph coloring
    for color in availableColors:
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
    
    # Add nodes to graph
    for node in adjList:
        G.add_node(node)
        for adj in adjList[node]:
            G.add_edge(node, adj)
    
    nodes = G.nodes()
    colors = [colorList[n] for n in nodes]
    nx.draw(G, node_color=colors, with_labels=True)
    plt.show()

# Main
gui = GraphVisualizerGUI(colorGraph)