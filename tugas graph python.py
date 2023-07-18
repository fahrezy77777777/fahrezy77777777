class Graph:
    def __init__(self, num_of_nodes):
        """
        Initializes Graph object with given number of nodes
        """
        self.adj_list = {}
        for i in range(num_of_nodes):
            self.adj_list[i] = []
   
    def add_edge(self, node1, node2):
        """
        Adds edge between two nodes
        """
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)
   
    def print_graph(self):
        """
        Prints out the graph in adjacency list format
        """
        for node in self.adj_list:
            print(node, "->", self.adj_list[node])
          
if __name__ == '__main__':
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    
    graph.print_graph()
