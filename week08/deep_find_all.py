graph = {'A': ['D', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}

from collections import deque
class BFS:
    def breadth_first_search_all(self, graph:dict, vertice, visited_nodes = []):
        all_occurences = []
        nonvisited_nodes = list(graph.keys())
        #list that includes all the occurences of the given key in the graph
        visited_nodes = []

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
            
                visited_nodes.append(new_node)
                if vertice in graph[new_node]:
                    all_occurences.append(graph[new_node])

                #we should start from the last one, which is on top of the queue, last in, first out
                for n in adjacent_nodes:
                    if n not in visited_nodes:
                        queue.appendleft(n)
        
        return all_occurences

class DFS:
    # finds the first appearance of the key in any of the dictionary values
    visited_nodes = []
    recursion_steps = []

    # Pick any unvisited vertex adjacent to the current vertex, and check to see if this is the goal.
    # If not, recursively apply the depth-first search to that vertex, 
    # ignoring any vertices that have already been visited.
    def depth_first_search_all(self, graph: dict, vertice):
        all_occurences = []
        self.visited_nodes = []
        self.recursion_steps = []

        # This is needed, because for example the first key might not have any values
        condition = True
        while condition:
            node = [x for x in list(graph.keys()) if x not in self.visited_nodes][0]
            self.recursion_steps = []
            result = self.inner(node, graph, vertice)
            
            if result:  
                # We get only the first execution return value of the recursion
                all_occurences.append(graph[self.recursion_steps[0]])
            
            # Stop execution once we have been in every vertice
            if [x for x in list(graph.keys()) if x not in self.visited_nodes] == []:
                condition = False

        return all_occurences

    # Recursive function which finds the appearance of the key in the current value
    def inner(self, node: str, graph: dict, vertice):
        self.visited_nodes.append(node)
        if vertice in graph[node]:
                self.recursion_steps.append(node)
                return True

        # As long as the key is not the current value, we check the values themselves for the same 
        for adj_node in graph[node]:
            if adj_node not in self.visited_nodes:
                if self.inner(adj_node, graph, vertice):
                    self.recursion_steps.append(adj_node)
                    return True

        return False

def main():
    bfs = BFS()
    dfs = DFS()

    print(bfs.breadth_first_search_all(graph, 'A'))
    print(dfs.depth_first_search_all(graph, 'A'))
    print(dfs.depth_first_search_all(graph, 'B'))

if __name__ == '__main__':
    main()
