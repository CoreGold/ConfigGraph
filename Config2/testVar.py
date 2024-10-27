import unittest
from var import get_dependencies, create_dependency_graph


class TestDependencyGraph(unittest.TestCase):

    def test_create_dependency_graph(self):

        test = create_dependency_graph('py3-trove-classifiers', 'Test')

        self.assertIn(test.body[0], '\t"py3-trove-classifiers"\n')
        self.assertIn(test.body[1], '\t"python3~3.12"\n')
        self.assertIn(test.body[2], '\t"py3-trove-classifiers" -> "python3~3.12"\n')
if __name__ == '__main__':
    unittest.main()
