import unittest
import os.path
from parse_log import readlog, main



class TestApp(unittest.TestCase):
    # def setUp(self) -> None:

    #     return super().setUp()
    def test_readlog(self):
        self.assertEqual(readlog('planning.log')[0],['Introduction', '09:20-11:00'])
        self.assertEqual(type(readlog('planning.log')),list)
        self.assertIsNotNone(readlog('planning.log'))
    
    def test_main(self):
        self.assertFalse(os.path.isfile("result.txt"))
        main("planning.log")
        self.assertTrue(os.path.isfile("result.txt"))

       
   




if __name__ == '__main__':
    unittest.main()