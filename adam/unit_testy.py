#!/usr/bin/python
import unittest
import wroc
import random

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
        
class testf3(unittest.TestCase):
    
    def testf3_1(self):
        w=wroc.f3(1)
        self.assertEqual(w,'jeden')
    
    def testf3_2(self):
        w=wroc.f3(2)
        self.assertEqual(w,'dwa')

    def testf3_3(self):
        w=wroc.f3(3)
        self.assertEqual(w,'trzy')
        
    def testf3_4(self): 
        w=wroc.f3(random.choice(range(4,1000)))
        self.assertEqual(w,'other')

class testf4(unittest.TestCase):
    
    def testf4_1(self):
        w=wroc.f4('ala')
        self.assertEqual(w,'ala ma kota')
    
    def testf4_2(self):
        w=wroc.f4('kot')
        self.assertEqual(w,'kot ma kota')

    def testf4_3(self):
        w=wroc.f4('kot', 'psa')
        self.assertEqual(w,'kot ma kota i psa')
        
    def testf4_4(self): 
        w=wroc.f4('kot', 'mysz')
        self.assertEqual(w,'kot ma kota i mysz')       
        
if __name__== '__main__':
    unittest.main()