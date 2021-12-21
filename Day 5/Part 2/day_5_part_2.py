from coords import *
from dots import *

x1 = 0
x2 = 0
y1 = 0
y2 = 0

def calculateDotMatrix(): #this gon hurt
    for coord in coordinates:
        x1 = coord[0]
        x2 = coord[2]
        y1 = coord[1]
        y2 = coord[3]
        
        if x1 == x2:
            if y2 > y1:
                for y in range(y1, y2 + 1):
                    if dots[y][x1] == '.':
                        dots[y][x1] = '1'
                    elif dots[y][x1] == '1':
                        dots[y][x1] = '2'
                    elif dots[y][x1] == '2':
                        dots[y][x1] = '3'
            else:
                for y in range(y1, y2 - 1, -1):
                    if dots[y][x1] == '.':
                        dots[y][x1] = '1'
                    elif dots[y][x1] == '1':
                        dots[y][x1] = '2'
                    elif dots[y][x1] == '2':
                        dots[y][x1] = '3'
        elif y1 == y2:
            if x2 > x1:
                for x in range(x1, x2 + 1):
                    if dots[y1][x] == '.':
                        dots[y1][x] = '1'
                    elif dots[y1][x] == '1':
                        dots[y1][x] = '2'
                    elif dots[y1][x] == '2':
                        dots[y1][x] = '3'
            else:
                for x in range(x1, x2 - 1, -1):
                    if dots[y1][x] == '.':
                        dots[y1][x] = '1'
                    elif dots[y1][x] == '1':
                        dots[y1][x] = '2'
                    elif dots[y1][x] == '2':
                        dots[y1][x] = '3'
        elif y1 != y2 and x1 != x2:
            if x2 > x1 and y2 > y1:
                while y1 <= y2 and x1 <= x2:
                    if dots[y1][x1] == '.':
                        dots[y1][x1] = '1'
                    elif dots[y1][x1] == '1':
                        dots[y1][x1] = '2'
                    elif dots[y1][x1] == '2':
                        dots[y1][x1] = '3'
                    x1 += 1
                    y1 += 1
            elif x2 < x1 and y2 < y1: 
                while y1 >= y2 and x1 >= x2:
                    if dots[y1][x1] == '.':
                        dots[y1][x1] = '1'
                    elif dots[y1][x1] == '1':
                        dots[y1][x1] = '2'
                    elif dots[y1][x1] == '2':
                        dots[y1][x1] = '3'
                    x1 -= 1
                    y1 -= 1
            elif x2 < x1 and y2 > y1: 
                while y1 <= y2 and x1 >= x2:
                    if dots[y1][x1] == '.':
                        dots[y1][x1] = '1'
                    elif dots[y1][x1] == '1':
                        dots[y1][x1] = '2'
                    elif dots[y1][x1] == '2':
                        dots[y1][x1] = '3'
                    x1 -= 1
                    y1 += 1
            elif x2 > x1 and y2 < y1: 
                while y1 >= y2 and x1 <= x2:
                    if dots[y1][x1] == '.':
                        dots[y1][x1] = '1'
                    elif dots[y1][x1] == '1':
                        dots[y1][x1] = '2'
                    elif dots[y1][x1] == '2':
                        dots[y1][x1] = '3'
                    x1 += 1
                    y1 -= 1
            else:
                print("UNREGISTERED COORDS: ", x1, x2, y1, y2)


def writeThatBadBoi():
    with open('C:/Users/parke/Documents/GitHub/Advent-of-Code-2021/Day 5/final.txt', 'w') as file:
        for i in dots:
            file.write(str(i) + '\n')

def nowCountThemTwos():
    the_counter = 0

    for i in dots:
        for z in i:
            if z == '3' or z == '2':
                the_counter += 1
    
    return the_counter

calculateDotMatrix()
writeThatBadBoi()

print("THE COUNTER: ", nowCountThemTwos())

#Making the txt file technically isn't necessary, only made it to fully test and also visualize how dope it is. 
#Please open "Done.txt" in notepad++ to get full experience. 
#Also please don't destroy me over copying and pasting code :( It very hard
