

import math
import random as rnd


MAX, MIN = math.inf, -math.inf


ID = input("Enter your BRACU ID: ")

if int(ID[3]) == 0:
    shufflecount = 8
else:
    shufflecount = int(ID[3])
    
    
mRange = int(ID[-1:-3:-1]) * 1.5
maxR = math.ceil(mRange)
winningPoint = int(ID[-1:-3:-1])
minR = int(ID[4])
array = []

x = 0

while x < 8:
    temp = rnd.randint(minR,maxR)
    array.append(temp)
    x += 1


def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):

    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:

        best = MIN

        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best
    else:
        best = MAX

        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex * 2 + i,
                          True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


optimal_list = []
count = 0
for i in range(shufflecount):
    rnd.shuffle(array)
    depth, node, boolean, array, alpha, beta = 0, 0, True, array, MIN, MAX
    optimal = minimax(depth, node, boolean, array, alpha, beta)
    optimal_list.append(optimal)
    if optimal > winningPoint:
        count += 1

print('Generated 8 random points between the minimum and maximum point limits:', array)
print('Total points to win:', winningPoint)
optimal_value = minimax(0, 0, True, array, MIN, MAX)
print('Achieved point by applying alpha-beta pruning =', optimal_value)
if optimal_value > winningPoint:
    print('The winner is Optimus Prime')
else:
    print('The winner is Megatron')
print('----------------After the shuffle----------------')
print('List of all points values from each shuffles:', optimal_list)
print('The maximum value of all shuffles:', max(optimal_list))
print('Won',count,'times out of 8 number of shuffles')

