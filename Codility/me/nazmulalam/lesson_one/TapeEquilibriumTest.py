'''
Created on 18 Oct 2015

@author: Nazmul Alam
'''
import unittest
from me.nazmulalam.lesson_one import TapeEquilibrium

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass

    def testEfficient(self):
        obj = TapeEquilibrium()
        A = [3, 1, 2, 4, 3]
        exp_result = 1
        result = obj.efficient(A)
        self.assertEquals(result, exp_result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
        