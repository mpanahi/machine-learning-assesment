import unittest
import sys
sys.path.insert(0, '../src')
from solution import *
class TestEvent(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.event_1 = Event('Phlake - MCH Herning Kongrescenter')

    def test_get_lineup(self):
        self.assertEqual(self.event_1.get_lineup(), {'Phlake': 100})

if __name__ == '__main__':
    unittest.main()
