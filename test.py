
import unittest
import pandas as pd
from assessment import number_orphan_star,find_planet
f=open('input.json')
data=pd.read_json(f)
f1=open('input1.json')
data1=pd.read_json(f1)


class test_assessment(unittest.TestCase):
    
    def test_number_orphan_star(self):
        self.assertEqual(number_orphan_star(data),0)
        self.assertEqual(number_orphan_star(data1),1)
    def test_find_planet(self):
        self.assertEqual(find_planet(data),"KOI-5800.01")
        self.assertEqual(find_planet(data1),'Kepler-633 b')
if __name__ == '__main__':
    unittest.main()