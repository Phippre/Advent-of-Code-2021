from input import *
import statistics

every_cost = []

position.sort()
the_goal = 0

for i in range(2000):
    total_cost = 0
    the_goal = i
    for z in range(len(position)):
        fuel_cost = 0
        increment = 1
        if position[z] >= the_goal:
            for x in range(position[z], the_goal, -1):
                fuel_cost += increment
                increment += 1
            total_cost += fuel_cost
        elif position[z] <= the_goal:
            for y in range(position[z], the_goal):
                fuel_cost += increment
                increment += 1
            total_cost += fuel_cost
    every_cost.append(total_cost)

print(min(every_cost))

#print(len(every_cost))
#every_cost.sort()
#print(every_cost)