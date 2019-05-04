import unittest
from deep_find import DFS, BFS

class TestDeepSearch(unittest.TestCase):

    graph = {'A': ['D', 'C', 'E'],
                'B': ['A', 'D', 'E'],
                'C': ['A', 'F', 'G'],
                'D': ['B'],
                'E': ['A', 'B', 'D'],
                'F': ['C'],
                'G': ['C']}

    def test_depth_first_search_when_no_such_vertice_in_the_graph_then_return_false(self):
        dfs = DFS()
        
        self.assertFalse(dfs.depth_first_search(self.graph, 'Z'))

    def test_depth_first_search_when_there_is_such_vertice_then_return_the_first_value_occurence(self):
        dfs = DFS()
        expected = ['A', 'D', 'E']
        self.assertEqual(dfs.depth_first_search(self.graph, 'A'), expected)

    def test_depth_first_search_when_the_vertice_is_in_the_value_of_the_first_key_and_there_is_no_recursion(self):
        dfs = DFS()
        expected = ['D', 'C', 'E']
        self.assertEqual(dfs.depth_first_search(self.graph, 'D'), expected)

    def test_breadth_first_search_when_no_such_vertice_is_in_the_grapth(self):
        bfs = BFS()
        self.assertFalse(bfs.breadth_first_search(self.graph, 'Z'))
    
    def test_breadth_first_search_when_there_is_such_vertice_and_return_its_value(self):
        bfs = BFS()
        expected = ['A', 'B', 'D']
        self.assertEqual(bfs.breadth_first_search(self.graph, 'A'), expected)


if __name__ == '__main__':
    unittest.main()