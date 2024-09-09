import unittest


def maximize_experience(n, a):
    dp = [0, -int(1e18)]
    for i in a:
        ndp = [0, 0]
        ndp[0] = max(dp[0], dp[1] + 2 * i)
        ndp[1] = max(dp[1], dp[0] + i)
        dp = ndp
    return max(dp)


class TestMaximizeExperience(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(maximize_experience(5, [1, 2, 3, 4, 5]), 22)

    def test_single_monster(self):
        self.assertEqual(maximize_experience(1, [10]), 10)

    def test_two_monsters(self):
        self.assertEqual(maximize_experience(2, [1, 100]), 201)

    def test_all_same_strength(self):
        self.assertEqual(maximize_experience(4, [5, 5, 5, 5]), 30)

    def test_large_numbers(self):
        self.assertEqual(
            maximize_experience(3, [1000000000, 1000000000, 1000000000]), 4000000000
        )

    def test_alternating_strength(self):
        self.assertEqual(maximize_experience(6, [1, 100, 1, 100, 1, 100]), 603)


if __name__ == "__main__":
    unittest.main()
