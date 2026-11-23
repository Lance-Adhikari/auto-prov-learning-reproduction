import unittest
from stage_02_log_clustering.embeddings_cosine_similarity import cosine_similarity, cosine_distance


class CosineTests(unittest.TestCase):
    def test_parallel(self):
        self.assertAlmostEqual(cosine_similarity([2, 3], [4, 6]), 1)
        self.assertAlmostEqual(cosine_distance([2, 3], [4, 6]), 0)

    def test_perpendicular(self):
        self.assertAlmostEqual(cosine_similarity([2, 3], [-3, 2]), 0)
        self.assertAlmostEqual(cosine_distance([2, 3], [-3, 2]), 1)

    def test_opposite(self):
        self.assertAlmostEqual(cosine_similarity([1, 0], [-1, 0]), -1)
        self.assertAlmostEqual(cosine_distance([1, 0], [-1, 0]), 2)

    def test_symmetry(self):
        self.assertAlmostEqual(cosine_similarity([1, 2, 3], [3, 0, 1]),
                               cosine_similarity([3, 0, 1], [1, 2, 3]))

    def test_large_and_small_coordinates(self):
        for scale in [1e300, 1e-300]:
            self.assertAlmostEqual(cosine_similarity([scale, scale], [1, 1]), 1)

    def test_invalid_vectors(self):
        for a, b in [([], []), ([0, 0], [1, 2]), ([1], [1, 2]),
                     ([[1, 2]], [[1, 2]]), ([float("nan")], [1]),
                     ([float("inf")], [1])]:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    cosine_similarity(a, b)


if __name__ == "__main__":
    unittest.main()
