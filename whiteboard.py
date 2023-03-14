def bus_stop(list):
    change = 0 
    for x in list: 
        change += x[0] - x[1] 

        print(change)
    
bus_stop([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])