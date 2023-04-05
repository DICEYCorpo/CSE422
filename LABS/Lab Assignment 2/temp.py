#
# def best(n,k,a):
#
#     count=(a-1)//k +1
#     print(count, end=" ")
#
# def worst(n,k,a):
#
#     possible_team=n//k
#     possible_team_without_you=possible_team-1
#
#     trry=a-1//2
#     if trry>=possible_team_without_you:
#         print(possible_team, )
#     else:
#         print(trry+1)
#
#
#
# iteration = int(input())
#
# for i in range(iteration):
#
#     info = (input().split())
#     total_players = int(info[0])
#     team_total_player = int(info[1])
#     alive = int(info[2])
#
#
#     for i in range(total_players):
#         temp = alive//i
#         if temp <= team_total_player:
#             break

MAX = 100
import numpy as np


# Return number of ways to which numbers
# that are greater than given number can
# be added to get sum.

def numberofways(n, m):
    dp = np.zeros((n + 2, n + 2))

    dp[0][n + 1] = 1

    # Filling the table. k is for numbers
    # greater than or equal that are allowed.
    for k in range(n, m - 1, -1):

        # i is for sum
        for i in range(n + 1):

            # initializing dp[i][k] to number
            # ways to get sum using numbers
            # greater than or equal k+1
            dp[i][k] = dp[i][k + 1]

            # if i > k
            if (i - k >= 0):
                dp[i][k] = (dp[i][k] + dp[i - k][k])
    return dp[n][m]
print(numberofways(9, 2))