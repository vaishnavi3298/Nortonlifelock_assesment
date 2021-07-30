
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
def find_number_planets(df):
    years=[]
    for x in df.DiscoveryYear:
        if(x not in years and x != ""):
            years.append(x)
    years.sort()
    for y in years:
        count = small=large=medium=0
        for x in df.DiscoveryYear:
            if(x == y and df.RadiusJpt[count]):
                if(df.RadiusJpt[count] < 1):
                    small=small+1
                if(df.RadiusJpt[count] < 2 and df.RadiusJpt[count] >= 1):
                    medium=medium+1
                if(df.RadiusJpt[count] > 2):
                    large=large+1
            count = count+ 1
        print("In %d,we discovered %d small planets, %d medium planets,and %d large planets" %(y,small,medium,large))
        

    