

#---------------------------------------------- QUESTION 1 ------------------------------------------------------------#


temp = []

with open('input.txt', 'r') as rf:
    for line in rf:
        create = line.split()
        temp.append(create)


def convert_magic(array):
    for row in range(len(array)):
        for col in range(len(array[0])):
            if array[row][col] == 'N':
                array[row][col] = 0
            else:
                array[row][col] = 1


def brain(array):
    combination1 = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    combination2 = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

    def dfs(row, col, array, pointer):
        if array[row][col] != 1:
            return pointer
        pointer += 1
        array[row][col] = 2000  # visited cells being denoted

        for x, y in zip(combination1, combination2):
            if (len(array) > row + x >= 0) and len(array[0]) > col + y >= 0:
                pointer = max(pointer, dfs(row + x, col + y, array, pointer))
        return pointer

    max_from_stranger_things = 0
    for row in range(len(array)):
        for col in range(len(array[0])):
            max_from_stranger_things = max(max_from_stranger_things, dfs(row, col, array, 0))
    return max_from_stranger_things


convert_magic(temp)
print(brain(temp))


#---------------------------------------------- QUESTION 1 ------------------------------------------------------------#


#---------------------------------------------- QUESTION 2 ------------------------------------------------------------#


from collections import deque

temp = []

with open('Question2 input1.txt', 'r') as rf:
    rf.seek(4)
    for line in rf:
        create = line.split()
        temp.append(create)


def convert_magic(array):
    for row in range(len(array)):
        for col in range(len(array[0])):
            if array[row][col] == 'A':
                array[row][col] = 2
            elif array[row][col] == 'H':
                array[row][col] = 1
            else:
                array[row][col] = 0 # Zeroes are set as traps


def bfs(grid):
    q = deque()
    time, human = 0, 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                human += 1
            if grid[row][col] == 2:
                q.append([row, col])
    combination1 = [0, 0, 1, -1]
    combination2 = [1, -1, 0, 0]
    newly_infected = None
    while q and human > 0:
        for i in range(len(q)):
            row, col = q.popleft()
            for x, y in zip(combination1, combination2):
                new_row, new_col = row+x, col+y

                if (new_row < 0 or new_row == len(grid) or new_col < 0 or new_col == len(grid[0])
                        or grid[new_row][new_col] in [0, 2]):
                    continue
                grid[new_row][new_col] = 2

                q.append([new_row, new_col])
                human -= 1
                newly_infected = True

        if newly_infected:
            time += 1
        newly_infected = False
    if human == 0:
        survival = 'No one survived.'
    else:
        survival = str(human) + ' survived'

    return time, survival


convert_magic(temp)
time, suvival = bfs(temp)
print('Time:', time, 'minutes')
print(suvival)


#---------------------------------------------- QUESTION 2 ------------------------------------------------------------#
