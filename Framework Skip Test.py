



import unittest

class suiteTest(unittest.TestCase):
   a = 50
   b = 40
   
   def testadd(self):
      """Add"""
      result = self.a+self.b
      self.assertEqual(result,100)

   @unittest.skipIf(a>b, "Skip over this routine")
   def testsub(self):
      """sub"""
      result = self.a-self.b
      self.assertTrue(result == -10)