import unittest 
from hello import * 

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), 'Hello, world !')

if __name__=="__main__":
   unittest.main()        
