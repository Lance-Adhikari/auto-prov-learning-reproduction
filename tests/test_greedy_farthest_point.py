import io
import unittest
from contextlib import redirect_stdout

from stage_02_log_clustering.greedy_farthest_point import greedy_farthest_point


class SamplingTests(unittest.TestCase):
    def sample(self, points, k):
        with redirect_stdout(io.StringIO()):
            return greedy_farthest_point(points, k)

    def test_uses_nearest_selected_distance(self):
        points = {"A": [1, 0], "B": [0.9, 0.1], "C": [0, 1],
                  "D": [-1, 0], "E": [0.1, 0.9]}
        self.assertEqual(self.sample(points, 3), ["A", "D", "C"])
        self.assertEqual(points["B"], [0.9, 0.1])
        self.assertEqual(list(points), ["A", "B", "C", "D", "E"])

    def test_ties_follow_insertion_order(self):
        points = {"start": [1, 0], "up": [0, 1], "down": [0, -1]}
        self.assertEqual(self.sample(points, 2), ["start", "up"])

    def test_single_and_all_samples(self):
        points = {"A": [1, 0], "B": [1, 0], "C": [-1, 0]}
        self.assertEqual(self.sample(points, 1), ["A"])
        self.assertEqual(self.sample(points, 3), ["A", "C", "B"])

    def test_invalid_sample_count(self):
        for k in [0, -1, 2, 1.5, True]:
            with self.subTest(k=k), self.assertRaises(ValueError):
                self.sample({"A": [1, 0]}, k)
        with self.assertRaises(ValueError):
            self.sample({}, 1)

    def test_validates_vectors_even_for_one_sample(self):
        for vector in [[0, 0], [], [1], [[1, 0]], [float("nan"), 0],
                       [float("inf"), 0]]:
            with self.subTest(vector=vector), self.assertRaises(ValueError):
                self.sample({"A": [1, 0], "B": vector}, 1)


if __name__ == "__main__":
    unittest.main()
