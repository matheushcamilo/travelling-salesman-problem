import unittest
from tsp import euclidean_distance, total_distance, brute_force_tsp


class TestTSP(unittest.TestCase):
    def test_euclidean_distance(self):
        self.assertAlmostEqual(euclidean_distance((0, 0), (3, 4)), 5.0)

    def test_total_distance(self):
        points = [(0, 0), (3, 4), (6, 8)]
        self.assertAlmostEqual(total_distance(points), 20.0)

    def test_brute_force_tsp(self):
        points = [(0, 0), (1, 1), (2, 2)]
        route, distance = brute_force_tsp(points)
        self.assertIsNotNone(route)
        self.assertGreater(distance, 0)


if __name__ == "__main__":
    unittest.main()
