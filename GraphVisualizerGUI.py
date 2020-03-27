import tkinter as tk
import tkinter.ttk as ttk
from InputsTab import *

class GraphVisualizerGUI:
    def __init__(self, callback):
        # Initalize main window
        self.masterWindow = tk.Tk(className="Graph visualizer")
        self.callerCallback = callback

        # Add notebook (tabs manager)
        self.masterNotebook = ttk.Notebook(self.masterWindow)
        self.masterNotebook.pack(expand=True)

        # Create inputs tab
        self.inputsTab = InputsTab(self.masterNotebook, self._callbackInput)

        self.masterWindow.mainloop()
    
    def _callbackInput(self, adjList):
        # adjList is a dict with int key and list value
        # what more does a caller need ? maybe return something ?
        # return a tuple, [0] is an image path for visuals
        self.callerCallback(adjList)
    