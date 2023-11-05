import unittest

import main

# 1. unittest.Testcase 상속 받아서 클라스 만들기
# 2. 테스트 하고자 하는 함수 return 값 받기
# unittest의 assert를 활용해서 테스트 통과하는지 확인


class myTest(unittest.TestCase):
    def test_helloworld(self):
        ret = main.helloworld("Myung")
        self.assertEqual(ret, "hellow world, Myung")


if __name__ == "__main__":
    unittest.main()
