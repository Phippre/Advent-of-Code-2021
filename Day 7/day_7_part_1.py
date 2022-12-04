from input import *
import statistics

position.sort()
the_goal = int(statistics.median(position))
print("The Median: ", the_goal)

fuel_cost = 0

while position[-1] != the_goal:
    for i in range(len(position)):
        if position[i] > the_goal:
            position[i] -= 1
            fuel_cost += 1
        if position[i] < the_goal:
            position[i] += 1
            fuel_cost += 1

print(fuel_cost)
