graph = {'A': ['D', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}


class BFS:
    def breath_first_search(self, data, key):
        pass


class DFS:
    # finds the first appearance of the key in any of the dictionary values
    def __init__(self):
        self.visited_nodes = []
        self.recursion_steps = []
        
    def depth_first_search(self, graph: dict, vertice, visited_nodes=[]):
        nonvisited_nodes = list(graph.keys())
        
        #this is needed, because for example the first key might not have any values
        for node in nonvisited_nodes:
            self.recursion_steps = []
            result = self.inner(node, graph, vertice)
            
            if result:  
                #we get only the first execution return value of the recursion
                return graph[self.recursion_steps[0]]

            nonvisited_nodes.remove(node)
        return False

    #recursive function which finds the appearance of the key in the current value
    def inner(self, node: str, graph: dict, vertice):
        if vertice in graph[node]:
                self.recursion_steps.append(node)
                return True

        #as long as the key is not the current value, we check the values themselves for the same 
        self.visited_nodes.append(node)
        for adj_node in graph[node]:
            if adj_node not in self.visited_nodes:
                if self.inner(adj_node, graph, vertice):
                    self.recursion_steps.append(adj_node)
                    return True

        return False

def main():
    bfs = BFS()
    bfs.breath_first_search(graph, 'A')

    dfs = DFS()
    print(dfs.depth_first_search(graph, 'A'))

if __name__ == '__main__':
    main()
