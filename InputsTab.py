import tkinter as tk
import tkinter.ttk as ttk
from collections import defaultdict

class InputsTab(ttk.Frame):
    def __init__(self, notebook, callback, title = "Graph input"):
        # Init
        super().__init__(notebook)
        self.iNumberOfEdges = None
        self.iNumberOfVerticies = None
        self.edgesInput = None
        self.callerCallback = callback

        # Add self to notebook
        notebook.add(self, text=title)

        # Add widgets
        self.addWidgets()
    
    def addWidgets(self):
        # number of verticies input
        tk.Label(self, text="Number of verticies: ").grid(row=0, column=0)
        self.iNumberOfVerticies = tk.Entry(self)
        self.iNumberOfVerticies.grid(row=0, column=1)

        # number of edges input
        tk.Label(self, text="Number of edges: ").grid(row=1, column=0)
        self.iNumberOfEdges = tk.Entry(self)
        self.iNumberOfEdges.grid(row=1, column=1)

        # input edges button
        tk.Button(self, text="Input edges", width=30,
         command= lambda: self._createEdgeInputs()).grid(row=2, column=0, columnspan=2, pady=(10,10))
        
        # generate button
        tk.Button(self, text="Generate!", width=30,
         command= lambda: self._generateEvent()).grid(row=4, column=0, columnspan=2, pady=(10,10))

    def _generateEvent(self):
        # Generate adj list
        try:
            nVerticies = int(self.iNumberOfVerticies.get())
            nEdges = int(self.iNumberOfEdges.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Values entered as edge/verticies are not integers")
            return
        relations = defaultdict(list)
        good = True
        # Create tuples of edges
        for i in range(nEdges):
            try:
                u = int(self.edgesInput.grid_slaves(row=i, column=0)[0].get())
                v = int(self.edgesInput.grid_slaves(row=i, column=1)[0].get())
                if(u > nVerticies or v > nVerticies):
                    raise Exception
            except ValueError:
                tk.messagebox.showerror("Error", "Values entered are not integers")
                good = False
                break
            except Exception:
                tk.messagebox.showerror("Error", "Values entered are bigger than the number of verticies")
                good = False
                break
            relations[u].append(v)
            # if undirected
            relations[v].append(u)
        if(good):
            self.callerCallback(relations)

    def _createEdgeInputs(self):
        if(self.edgesInput != None):
            self.edgesInput.grid_forget()
            self.edgesInput.destroy()

        # edges input
        self.edgesInput = tk.Frame(self)
        self.edgesInput.grid(row=3, column=0, columnspan=2, pady=(5, 10))
        try:
            nVerticies = int(self.iNumberOfVerticies.get())
            nEdges = int(self.iNumberOfEdges.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Values entered as edge/verticies are not integers")
            return
        InputsTab.createTableInput(self.edgesInput, 2, nEdges, 8)

    @staticmethod
    def createTableInput(frame, width, height, cellSize):
        for i in range(height):
            for j in range(width):
                tk.Entry(frame, width=cellSize).grid(row=i, column=j)
