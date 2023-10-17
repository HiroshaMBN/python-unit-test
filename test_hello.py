import unittest
import hello

class HelloTest(unittest.TestCase):
    def testHelloWorld(self):
        # self.assertEqual(hello.helloWorld(), 'hello world')
       
        i = 55
        self.assertEqual(hello.helloWorld() , i)
        # self.assertEqual(hello.helloWorld(), "None")

#run unit test
if __name__ == '__main__':
    unittest.main()