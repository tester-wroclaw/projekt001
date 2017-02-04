#!/usr/bin/python
import unittest
import wroc

class testdd(unittest.TestCase):
    
    def testf1(self):
        w=wroc.f1(0)
        self.assertEqual(w,0)

    def testf2(self):
        w=wroc.f1(1)
        self.assertEqual(w,1)
        
    def testf3(self):
        w=wroc.f1(2)
        self.assertEqual(w,4)
        
    def testf4(self):
        w=wroc.f1(2,1)
        self.assertEqual(w,5)
        
    def testf5(self):
        w=wroc.f1(2,3)
        self.assertEqual(w,7)
        
if __name__== '__main__':
    unittest.main()