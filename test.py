# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 23:40:43 2021

@author: HP Customer
"""
import unittest
import pandas as pd
from assessment import number_orphan_star,find_planet
f=open('input.json')
data=pd.read_json(f)
f1=open('input1.json')
data1=pd.read_json(f1)
#f2=open('input2.json')
#data2=pd.read_json(f2)



class test_assessment(unittest.TestCase):
    
    def test_number_orphan_star(self):
        self.assertEqual(number_orphan_star(data),2)
        self.assertEqual(number_orphan_star(data1),0)
        #self.assertEqual(number_orphan_star(data2),1)
    def find_planet(self):
        self.assertEqual(find_planet(data),"Kepler-9 b")
        self.assertEqual(find_planet(data),"Kepler-1346 b")
        
if __name__ == '__main__':
    unittest.main()