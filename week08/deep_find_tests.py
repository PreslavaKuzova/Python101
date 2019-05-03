import unittest
from deep_find import DFS

class TestDeepSearch(unittest.TestCase):    
    def test_depth_first_search_when_no_such_vertice_in_the_graph_then_return_false(self):
        dfs = DFS()
        graph = {'A': ['D', 'C', 'E'],
                'B': ['A', 'D', 'E'],
                'C': ['A', 'F', 'G'],
                'D': ['B'],
                'E': ['A', 'B', 'D'],
                'F': ['C'],
                'G': ['C']}
        self.assertFalse(dfs.depth_first_search(graph, 'Z'))

    def test_depth_first_search_when_there_is_such_vertice_then_return_the_first_value_occurence(self):
        dfs = DFS()
        graph = {'A': ['D', 'C', 'E'],
                'B': ['A', 'D', 'E'],
                'C': ['A', 'F', 'G'],
                'D': ['B'],
                'E': ['A', 'B', 'D'],
                'F': ['C'],
                'G': ['C']}
        expected = ['A', 'D', 'E']
        self.assertEqual(dfs.depth_first_search(graph, 'A'), expected)

    def test_depth_first_search_when_the_vertice_is_in_the_value_of_the_first_key_and_there_is_no_recursion(self):
        dfs = DFS()
        graph = {'A': ['D', 'C', 'E'],
                'B': ['A', 'D', 'E'],
                'C': ['A', 'F', 'G'],
                'D': ['B'],
                'E': ['A', 'B', 'D'],
                'F': ['C'],
                'G': ['C']}
        expected = ['D', 'C', 'E']
        self.assertEqual(dfs.depth_first_search(graph, 'D'), expected)

if __name__ == '__main__':
    unittest.main()