import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_none(self):      #used for checking None statement in max_list_iter
        self.assertEqual(max_list_iter([]), None)

    def test_max_list_iter_num(self):       #used for checking regular max_list_iter inputs
        self.assertEqual(max_list_iter([1, 2, 3, 4]), 4)
        self.assertEqual(max_list_iter([5, 3, 2, 1, 0]), 5)
        self.assertEqual(max_list_iter([4, 3, 5, 1]), 5)
        self.assertEqual(max_list_iter([7]), 7)
        self.assertEqual(max_list_iter([2, 2]), 2)

    def test_reverse_rec(self):             #used for checking regular reverse_rec inputs
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([5, 7, 3, 9]), [9, 3, 7, 5])
        self.assertEqual(reverse_rec([1, 1]), [1, 1])

    def test_reverse_rec_none(self):        #used for testing empty reverse_rec list
        self.assertEqual(reverse_rec([]), [])

    def test_reverse_rec_error(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_bin_search(self):              #given test function
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

    def test_bin_search_case(self):         #used for checking regular bin_searches
        self.assertEqual(bin_search(5, 0, 8, [1, 3, 5, 6, 8, 10, 12, 14, 16]), 2)
        self.assertEqual(bin_search(1, 0, 6, [1, 3, 5, 6, 8, 10, 12]), 0)
        self.assertEqual(bin_search(12, 0, 6, [1, 3, 5, 6, 8, 10, 12]), 6)
        self.assertEqual(bin_search(3, 0, 1, [1, 3]), 1)
        self.assertEqual(bin_search(1, 0, 1, [1, 3]), 0)
        self.assertEqual(bin_search(2, 0, 0, [2]), 0)

    def test_bin_search_none(self):         #used for checking the None statement in bin_search
        self.assertEqual(bin_search(10, 0, 5, [1, 2, 3, 4, 5, 6]), None)
        self.assertEqual(bin_search(2, 0, 0, [1]), None)
        self.assertEqual(bin_search(2, 0, 0, [1, 6]), None)
        self.assertEqual(bin_search(2, 0, 0, []), None)

    def test_bin_search_error(self):        #used for checking the raise valueerror in bin_search
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(1, 0, 0, tlist)

if __name__ == "__main__":
        unittest.main()

    
