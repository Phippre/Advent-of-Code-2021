from thelist import *

def checkY():
    callnum = 5
    x = 0
    y = 0
    print(len(numbers))
    for num in numbers[0:85]: #20 is the first solve 86 is the second.
        for y, table in enumerate(bingo):
            for x, row in enumerate(table):
                for i, s in enumerate(row):
                    if s == num:
                        bingo[y][x][i] = "X"
                    
                
checkY()

for y in range(len(bingo)):
    for x in range(0, 5):
        print(bingo[y][x], sep="\n")
    print("\n")
