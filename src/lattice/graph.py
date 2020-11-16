import numpy as np

class Graph:

    def __init__(self, adj, vals):
        self.adjacency_matrix = adj
        self.node_values = vals

    def set_val(self, index, new_val):
        self.node_values[index] = new_val
    
    def get_val(self, index):
        return self.node_values[index]

    def get_adj(self, index):
        return self.adjacency_matrix[index]
    
    val = get_val
    adj = get_adj