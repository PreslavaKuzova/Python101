import unittest
from deep_find_all import DFS, BFS

class TestDeepSearch(unittest.TestCase):

    graph = {'A': ['D', 'C', 'E'],
                'B': ['A', 'D', 'E'],
                'C': ['A', 'F', 'G'],
                'D': ['B'],
                'E': ['A', 'B', 'D'],
                'F': ['C'],
                'G': ['C']}

    def test_depth_first_search_when_no_such_vertice_in_the_graph_then_return_empty_list(self):
        dfs = DFS()
        expected = []
        self.assertEqual(dfs.depth_first_search_all(self.graph, 'Z'), expected)

    def test_breadth_first_search_when_no_such_vertice_then_return_empty_list(self):
        bfs = BFS()
        expected = []
        self.assertEqual(bfs.breadth_first_search_all(self.graph, 'Z'), expected)
    
    def test_breadth_first_search_when_there_is_such_vertice_then_return_list_of_all_values_containing_it(self):
        bfs = BFS()
        expected = [['A', 'B', 'D'], ['A', 'F', 'G'], ['A', 'D', 'E']]
        self.assertEqual(bfs.breadth_first_search_all(self.graph, 'A'), expected)

    def test_depth_first_search_when_there_is_such_vertice_then_return_list_of_all_values_containing_it(self):
        dfs = DFS()
        expected = [['A', 'D', 'E'], ['A', 'F', 'G'], ['A', 'B', 'D']]
        self.assertEqual(dfs.depth_first_search_all(self.graph, 'A'), expected)

    def test_breadth_and_depth_first_search_for_the_same_vertice_and_compare_the_results_then_return_true(self):
        bfs = BFS()
        dfs = DFS()
        bfs_result = bfs.breadth_first_search_all(self.graph, 'A')
        dfs_result = dfs.depth_first_search_all(self.graph, 'A')
        # In order to compare the equality, we need to order them first
        self.assertEqual(bfs_result.sort(), dfs_result.sort())
        

if __name__ == '__main__':
    unittest.main()