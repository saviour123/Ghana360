import unittest
import app


class AppTestMethods(unittest.TestCase):

    def test_sendmessage(self):
        self.assertEqual(app.sendMessage("hello"), type)


if __name__ == '__main__':
    unittest.main()
