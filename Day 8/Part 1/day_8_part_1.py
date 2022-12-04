from inputdata import *

counter = 0

top = ""
top_left = ""
top_right = ""
middle = ""
bottom_left = ""
bottom_right = ""
bottom = ""

def processOne():
    global top_right, bottom_right

    for i in input_data[0]:
        if len(i) == 2: # Make 7
            top_right = i[0]
            bottom_right = i[1]
    
    print(top_right, bottom_right)

def processSeven():
    global top, top_right, top_left

    for i in input_data[0]:
        if len(i) == 3:
            for z in i:
                if z != top_right and z != bottom_right:
                    top = z
    print(top, top_right, bottom_right)
            
                

processOne()
processSeven()