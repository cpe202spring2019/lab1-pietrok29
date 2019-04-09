import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("LA", 79.5, -110.1)
        loc2 = Location("T", 100.0, 0)
        loc3 = loc1
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc1), "Location('LA', 79.5, -110.1)")
        self.assertEqual(repr(loc2), "Location('T', 100.0, 0)")

    def test_eq(self):
    	loc1 = Location("LA", 79.5, -110.1)
    	loc2 = Location("T", 100.0, 0)
    	loc3 = loc1
    	loc4 = Location("T", 100.0, 0)
    	self.assertEqual(loc1 == loc3, True)
    	self.assertEqual(loc1 == loc2, False)
    	self.assertEqual(loc4 == loc2, True)

    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
