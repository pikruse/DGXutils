import unittest
from DGXutils import GetLowestGPU, GetFileNames

class TestDGXutils(unittest.TestCase):
    def test_GetLowestGPU(self):
        self.assertEqual(GetLowestGPU() in ['cuda:0', 'cuda:1', 'cuda:2', 'cuda:3', 'cuda:4', 'cuda:5', 'cuda:6', 'cuda:7', 'cpu'], True)

    def test_GetFileNames(self):
        self.assertEqual(GetFileNames('test_dir', '.txt'), ["test.txt"])