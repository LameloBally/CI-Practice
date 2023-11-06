import unittest

import good


class helloTest(unittest.TestCase):
    def test_hello(self):
        ret = good.Hello("Myung")
        self.assertEqual(ret, "Hello Nice to mee u, Maung")


if __name__ == "__main__":
    unittest.main()
