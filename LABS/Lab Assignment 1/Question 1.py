

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
        array[row][col] = 2000  #visited cells being denoted

        for x, y in zip(combination1, combination2):
            if (len(array) > row + x >= 0) and len(array[0]) > col+y >= 0:
                pointer = max(pointer, dfs(row+x, col+y, array, pointer))
        return pointer

    max_from_stranger_things = 0
    for row in range(len(array)):
        for col in range(len(array[0])):
            max_from_stranger_things = max(max_from_stranger_things, dfs(row, col, array, 0))
    return max_from_stranger_things


convert_magic(temp)
print(brain(temp))
