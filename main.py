
import pandas as pd
from assessment import number_orphan_star,find_planet,find_number_planets
url = "https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a/raw/9a196385b44d4288431eef74896c0512bad3defe/exoplanets"
df = pd.read_json(url)
orphan_star=number_orphan_star(df)
print("Number of orphan stars:%d"%(orphan_star))
planet=find_planet(df)
print("Planet orbitting the hottest star:%s"%(planet))
find_number_planets(df)