def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

import unittest

class TestQuickSort(unittest.TestCase):
    
    def test_positive_cases(self):
        self.assertEqual(quick_sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(quick_sort([1]), [1])
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_negative_cases(self):
        with self.assertRaises(TypeError):
            quick_sort(['a', 'b', 'c'])
        with self.assertRaises(TypeError):
            quick_sort([None])
    
    def test_performance_cases(self):
        import time
        large_array = list(range(10000, 0, -1))
        start_time = time.time()
        quick_sort(large_array)
        end_time = time.time()
        self.assertTrue((end_time - start_time) < 1) # Ensure it sorts within 1 second
    
    def test_boundary_cases(self):
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([1]), [1])
        self.assertEqual(quick_sort([2, 2, 2]), [2, 2, 2])
    
    def test_idempotency_cases(self):
        array = [3, 6, 8, 10, 1, 2, 1]
        sorted_array = quick_sort(array)
        self.assertEqual(sorted_array, quick_sort(sorted_array))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
