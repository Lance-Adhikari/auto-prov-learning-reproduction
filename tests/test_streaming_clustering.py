import unittest

import numpy as np

from stage_02_log_clustering.streaming_clustering import streaming_cluster


class StreamingTests(unittest.TestCase):
    def test_threshold_experiment(self):
        points = [[1, 1], [1.1, 1.1], [0.9, 1], [5, 5],
                  [5.1, 5], [9, 1], [9.1, 1.1]]
        for threshold, expected in [(0.1, 5), (0.5, 3), (10, 1)]:
            with self.subTest(threshold=threshold):
                clusters = streaming_cluster(points, threshold)
                self.assertEqual(len(clusters), expected)
                self.assertEqual(sum(len(c["points"]) for c in clusters), 7)
        clusters = streaming_cluster(points, 0.5)
        self.assertEqual([len(c["points"]) for c in clusters], [3, 2, 2])
        np.testing.assert_allclose(clusters[0]["center"], [1, 3.1 / 3])

    def test_updated_center_and_inclusive_boundary(self):
        clusters = streaming_cluster([[0], [2], [3]], 2)
        self.assertEqual(len(clusters), 1)
        np.testing.assert_allclose(clusters[0]["center"], [5 / 3])

    def test_nearest_cluster_and_tie(self):
        clusters = streaming_cluster([[0], [4], [2]], 2)
        self.assertEqual([len(c["points"]) for c in clusters], [2, 1])
        clusters = streaming_cluster([[0], [4], [3.5]], 1)
        self.assertEqual([len(c["points"]) for c in clusters], [1, 2])

    def test_empty_and_zero_threshold(self):
        self.assertEqual(streaming_cluster([], 0), [])
        self.assertEqual(len(streaming_cluster([[1], [1], [2]], 0)), 2)

    def test_does_not_alias_input(self):
        point = np.array([1., 2.])
        clusters = streaming_cluster([point], 1)
        point[0] = 99
        np.testing.assert_array_equal(clusters[0]["points"][0], [1, 2])
        np.testing.assert_array_equal(clusters[0]["center"], [1, 2])

    def test_invalid_inputs(self):
        for threshold in [-1, float("nan"), float("inf"), [1]]:
            with self.subTest(threshold=threshold), self.assertRaises(ValueError):
                streaming_cluster([], threshold)
        for points in [[[]], [[[1]]], [[float("nan")]],
                       [[float("inf")]], [[1, 2], [1]]]:
            with self.subTest(points=points), self.assertRaises(ValueError):
                streaming_cluster(points, 1)


if __name__ == "__main__":
    unittest.main()
