# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import json
import numpy as np

#function to find number of orphan stars
def number_orphan_star(json_file):
    orphan_planet_count=0
    for x in json_file.TypeFlag:
        if(x == 3):
            orphan_planet_count = orphan_planet_count+1
    return orphan_planet_count

#function to identify the planet orbiting the hottest star
def find_planet(json_file):
    count=index=hottest_star=0
    for x in json_file.HostStarTempK:
        if(x!="" and x > hottest_star):
            hottest_star = x
            index = count
            count = count + 1
    return (json_file.PlanetIdentifier[index])

#function to find and display timeline of the number of planets discovered per year
def find_number_planets(json_file):
    years=[]
    for x in json_file.DiscoveryYear:
        if(x not in years and x != ""):
            years.append(x)
    years.sort()
    for y in years:
        count = small=large=medium=0
        for x in json_file.DiscoveryYear:
            if(x == y and json_file.RadiusJpt[count]):
                if(json_file.RadiusJpt[count] < 1):
                    small=small+1
                if(json_file.RadiusJpt[count] < 2 and json_file.RadiusJpt[count] >= 1):
                    medium=medium+1
                if(json_file.RadiusJpt[count] > 2):
                    large=large+1
            count = count+ 1
        print("In %d,we discovered %d small planets, %d medium planets,and %d large planets" %(y,small,medium,large))
        

#main function
#url = "https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a/raw/9a196385b44d4288431eef74896c0512bad3defe/exoplanets"
#df = pd.read_json(url)
#orphan_star=number_orphan_star(df)
#print("Number of orphan stars:%d"%(orphan_star))
#planet=find_planet(df)
#print("Planet orbitting the hottest star:%s"%(planet))
#find_number_planets(df)
    
