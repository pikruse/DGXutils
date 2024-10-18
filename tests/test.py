import unittest
from DGXutils import GetLowestGPU, GetFileNames

class TestDGXutils(unittest.TestCase):
    def test_GetLowestGPU(self):
        out = GetLowestGPU()
        self.assertTrue(out == 'cpu' or out.startswith('cuda:'))

    def test_GetFileNames(self):
        self.assertEqual(GetFileNames('test_dir', '.txt'), ["test.txt"])

if __name__ == '__main__':
    unittest.main()