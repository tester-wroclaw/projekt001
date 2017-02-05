#!/usr/bin/python
import unittest
import wroc

class testdd(unittest.TestCase):
    
<<<<<<< HEAD
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
=======

>>>>>>> branch 'master' of https://github.com/tester-wroclaw/projekt001.git
        w=wroc.f1(2,3)
        self.assertEqual(w,7)
        
if __name__== '__main__':
    unittest.main()