# src/contextual_graph.py

class ContextualGraph:
    def __init__(self):
        # Initialize the contextual graph as a dictionary to store graph IDs and their corresponding graphs
        self.graphs = {}

    def add_graph(self, graph_id, graph):
        # Add a contextual graph to the existing graph
        if graph_id in self.graphs:
            raise ValueError(f"Graph with ID {graph_id} already exists.")
        self.graphs[graph_id] = graph

    def get_graph(self, graph_id):
        # Retrieve a contextual graph based on the graph ID
        if graph_id not in self.graphs:
            raise KeyError(f"Graph with ID {graph_id} does not exist.")
        return self.graphs[graph_id]

    def update_graph(self, graph_id, updated_graph):
        # Update a contextual graph based on the graph ID
        if graph_id not in self.graphs:
            raise KeyError(f"Graph with ID {graph_id} does not exist.")
        self.graphs[graph_id] = updated_graph

    def delete_graph(self, graph_id):
        # Delete a contextual graph based on the graph ID
        if graph_id not in self.graphs:
            raise KeyError(f"Graph with ID {graph_id} does not exist.")
        del self.graphs[graph_id]

    def get_all_graph_ids(self):
        # Return a list of all graph IDs in the contextual graph
        return list(self.graphs.keys())

