# Project: Miles Per Hour Project
# Author: Joshua Buck
# Date: 02/28/2021
# Project to visualize effects of decreasing time driven based on incremental increasing speed, starting at various speeds.


# Creating 
def incrementor(start_speed, increment):
    "(float,float) -> list"
    
    i = 0
    times = list()
    while i < 100:
        spd = i
        v = list() 
        spd += increment
        percent_of_time = start_speed/spd
        v =  [i,spd,percent_of_time]
        times[i] = v
        i += 1
    return times
#
    spd = start_speed
    times = list()
    if spd < 100:
        
        
    

        
        
