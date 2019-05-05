graph = {'A': ['D', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}

from collections import deque
def breadth_first_update(graph:dict, vertice, new_value):
    visited_nodes = []

    # This is needed, because for example the first key might not have any values
    for node in list(graph.keys()):
        queue = deque([node])
        adjacent_nodes = (graph[node])[::-1]
        
        # Breadth-first search prefers to visit the neighbors 
        # of earlier visited nodes before the neighbors of more recently visited ones
        while len(queue) > 0:
            new_node = queue.pop()
            if new_node in visited_nodes:
                continue
        
            visited_nodes.append(new_node)
            # We change the value of the given vertice to new_value only in the values of the graph
            if vertice in graph[new_node]:
                graph[new_node] = [x if x != vertice else new_value for x in graph[new_node]]

            #we should start from the last one, which is on top of the queue, last in, first out
            for n in adjacent_nodes:
                if n not in visited_nodes:
                    queue.appendleft(n)
    
    return graph

def main():
    print(breadth_first_update(graph, 'A', 'H'))

if __name__ == '__main__':
    main()