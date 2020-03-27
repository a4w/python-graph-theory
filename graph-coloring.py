def colorGraph(adjList):
    colors = ["#F00", "#0F0", "#00F", "#0FF"]
    colorList = dict()
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
    
    return colorList

test = dict()
test[1] = [2,3,4]
test[2] = [1, 4]
test[3] = [1]
test[4] = [2,1]
print(colorGraph(test))
