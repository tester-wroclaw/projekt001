#!/usr/bin/python
import unittest
import wroc

class testf1(unittest.TestCase):
    
    def testf1_1(self):
        w=wroc.f1(0)
        self.assertEqual(w,0)

    def testf1_2(self):
        w=wroc.f1(1)
        self.assertEqual(w,1)
        
    def testf1_3(self):
        w=wroc.f1(2)
        self.assertEqual(w,4)
        
    def testf1_4(self):
        w=wroc.f1(2,1)
        self.assertEqual(w,5)
        
    def testf1_5(self):
        w=wroc.f1(2,3)
        self.assertEqual(w,7)
        
class testf2(unittest.TestCase):
    
    def testf2_1(self):
        w=wroc.f2('ala')
        self.assertEqual(w,'a')
        
    def testf2_2(self):
        w=wroc.f2([1,2,3])
        self.assertEqual(w,1)
        
    def testf2_3(self):
        w=wroc.f2([])
        self.assertEqual(w,'BUUUUM')
        
if __name__== '__main__':
    unittest.main()