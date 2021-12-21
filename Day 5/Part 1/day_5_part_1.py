from coords import *
from dots import *
import pickle

x1 = 0
x2 = 0
y1 = 0
y2 = 0

real_coords = []

def organizeCoordinates(values):
    global real_coords

    for i in values:
        if i[0] == i[2] or i[1] == i[3]:
            real_coords.append(i)

def calculateDotMatrix(): #this gon hurt
    for coord in real_coords:
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
            else:
                for y in range(y1, y2 - 1, -1):
                    if dots[y][x1] == '.':
                        dots[y][x1] = '1'
                    elif dots[y][x1] == '1':
                        dots[y][x1] = '2'
        elif y1 == y2:
            if x2 > x1:
                for x in range(x1, x2 + 1):
                    if dots[y1][x] == '.':
                        dots[y1][x] = '1'
                    elif dots[y1][x] == '1':
                        dots[y1][x] = '2'
            else:
                for x in range(x1, x2 - 1, -1):
                    if dots[y1][x] == '.':
                        dots[y1][x] = '1'
                    elif dots[y1][x] == '1':
                        dots[y1][x] = '2'

def writeThatBadBoi():
    with open('C:/Users/parke/Documents/GitHub/Advent-of-Code-2021/Day 5/final.txt', 'w') as file:
        for i in dots:
            file.write(str(i) + '\n')

def nowCountThemTwos():
    two_counter = 0

    for i in dots:
        for z in i:
            if z == '2':
                two_counter += 1
    
    return two_counter



organizeCoordinates(coordinates)
calculateDotMatrix()
writeThatBadBoi()

print("TWOS: ", nowCountThemTwos())

#Making the txt file technically isn't necessary, only made it to fully test and also visualize how dope it is. 
#Please open "Done.txt" in notepad++ to get full experience. 
#Also please don't destroy me over copying and pasting code :( It very hard
