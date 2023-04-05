

import random as rnd
import math 
shuffleneeded = 8
minRange = 0

storedarray = []
studentID = int(input())

tempID = studentID
MAX, MIN = math.inf, -math.inf
for i in range(3):
    tempID = tempID//10
    temp = tempID % 10

    minRange = temp
studentID = str(studentID)
maxRange = math.ceil(int(studentID[-1:-3:-1]) * 1.5)
winningPoint = int(studentID[-1:-3:-1])




for i in range(0, 8):
    temp = rnd.randint(minRange,maxRange)
    storedarray.append(temp)



def shuffle(depth, node, boolean, arr, alpha, beta):
    optimal_array = []
    for i in range(shuffleneeded):
        rnd.shuffle(arr)
        depth, node, boolean, storedarray, alpha, beta = 0, 0, True, arr, MIN, MAX
        optimal = winner(depth, node, boolean, storedarray, alpha, beta)
        optimal_array.append(optimal)
    return optimal_array

def winner(depth, node, boolean, values, alpha, beta):
    if depth == 3:
        return values[node]

    if boolean:
        best = MIN
        for i in range(0, 2):
            val = winner(depth + 1, node * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = MAX
        for i in range(0, 2):
            val = winner(depth + 1, node * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

print('Generated 8 random points between the minimum and maximum point limits:', storedarray)
print('Total points to win:', winningPoint)
optimal_value = winner(0, 0, True, storedarray, MIN, MAX)
print('Achieved point by applying alpha-beta pruning =', optimal_value)
if optimal_value > winningPoint:
    print('The winner is Optimus Prime')
else:
    print('The winner is Megatron')
print()
print('After the shuffle:')
optimal_array = shuffle(0, 0, True, storedarray, MIN, MAX)
print('List of all points values from each shuffles:', optimal_array)
print('The maximum value of all shuffles:', max(optimal_array))
count = 0
for i in optimal_array:
    if i > winningPoint:
        count += 1
print('Won',count,'times out of 8 number of shuffles')
