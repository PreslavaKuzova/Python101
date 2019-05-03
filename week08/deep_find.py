graph = {'A': ['D', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}

from collections import deque
class BFS:
    def breadth_first_search(self, graph:dict, vertice,visited_nodes = set()):
        nonvisited_nodes = list(graph.keys())

        # This is needed, because for example the first key might not have any values
        for node in nonvisited_nodes:
            queue = deque([node])
            adjacent_nodes = (graph[node])[::-1]
            
            # Breadth-first search prefers to visit the neighbors 
            # of earlier visited nodes before the neighbors of more recently visited ones
            while len(queue) > 0:
                new_node = queue.pop()
                
                if new_node in visited_nodes:
                    continue
            
                visited_nodes.add(new_node)
                if vertice in graph[new_node]:
                    return graph[new_node]

                #we should start from the last one, which is on top of the queue, last in, first out
                for n in adjacent_nodes:
                    if n not in visited_nodes:
                        queue.appendleft(n)

        return False

class DFS:
    # finds the first appearance of the key in any of the dictionary values
    def __init__(self):
        self.visited_nodes = []
        self.recursion_steps = []
    # Pick any unvisited vertex adjacent to the current vertex, and check to see if this is the goal.
    # If not, recursively apply the depth-first search to that vertex, 
    # ignoring any vertices that have already been visited.
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
    dfs = DFS()

    # Results are different because the algorithm for the depth and breath first search work
    # differently and there is more than one occurence of 'A' in our graph
    print(bfs.breadth_first_search(graph, 'A'))
    print(dfs.depth_first_search(graph, 'A'))

    # As long as there is only one occurence in the graph, results are the same
    print(bfs.breadth_first_search(graph, 'F'))
    print(dfs.depth_first_search(graph, 'F'))

if __name__ == '__main__':
    main()

