#eight_puzzle.py

#Usage Examples:
#python -i eight_puzzle.py
#>>> problem = EightPuzzleSearchProblem([[7, 2, 4], [5, 0, 6], [8, 3, 1]])
#>>> actions = bfs(problem)
#>>> print(actions)
#>>> problem.showResults(actions)
#>>> actions = AStarSearch(problem, problem.tilesHeuristic)
#>>> actions = AStarSearch(problem, problem.manHattanHeuristic)

#Attribution information: written by Mursalin Habib (mursalin.habib@bracu.ac.bd) as for CSE422 at Brac University



from collections import deque

import heapq

class Queue:

    """Implementation of queue data structure. You don't have to know how all of this works.
    The only important thing is that you know that push() and pop() work in a FIFO manner.
    
    
    
    >>> queue = Queue()
    >>> queue.push(4)
    >>> queue.push(2)
    >>> queue.push(7)
    >>> a = queue.pop()
    >>> a == 4
    True
    >>> queue.isEmpty()
    False
    >>> queue.pop()
    2
    >>> queue.pop()
    7
    >>> queue.isEmpty()
    True"""


    def __init__(self):
        self.queue = deque()
        self.count = 0

    def push(self, item):
        self.queue.append(item)
        self.count += 1

    def pop(self):
        self.count -= 1
        return self.queue.popleft()
    def popright(self):
        self.count -= 1
        return self.queue.pop()

    def isEmpty(self):
        return self.count == 0


class PriorityQueue:

    """Implementation of a min-priority queue. Just like Queue, you don't have to understand how all of this works.
    The only thing you have to know is that when you call pop(), the item with the smallest priority value is returned.
    
    pop() and isEmpty() have the same signature as before. push() now takes two things as input: an item and a priority."""



    def __init__(self):
        self.heap = []
        self.count = 0
        self.index = 0
    
    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, self.index, item))
        self.index += 1
        self.count += 1

    def pop(self):
        self.count -= 1
        _, _, item = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return self.count == 0 





class SearchProblem:

    """The template of a general search problem. Any class that extends SearchProblem promises to the outside world that it has implemented the following four methods.
    See EightPuzzleSearchProblem below for an example."""



    def getStartState(self):
        """Returns the start state for the problem. Search algorithms will call this method."""
        pass

    def isGoal(self, state):
        """Takes a state as input and returns True only if the state is a goal. What constitutes a goal will depend on the problem."""
        pass

    def getSuccessors(self, state):
        """Takes a state as input and returns a list of (successor, action stepCost) triples.
        
        If the method returns [(succ1, action1, cost1), (succ2, action2, cost2), succ3, action3, cost3)], 
        then state has three available actions: action1, action2, and action3 with costs cost1, cost2, and cost3 respectively.
        Taking action1, action2, and action3 at state takes you to states succ1, succ2, and succ3 respectively."""
        pass

    def getCostOfActions(self, actions):
        """Takes a list of actions as input and returns the total cost of those actions."""
        pass


class EightPuzzleState:

    """A helper class for EightPuzzleSearchProblem (see below). Encodes the information required to represent a state for an eight puzzle board.
     Instances of EightPuzzleState should not be created outside of EightPuzzleSearchProblem."""

    def __init__(self, cells):

        """
        >>> state = EightPuzzleState([[7, 2, 4], [5, 0, 6], [8, 3, 1]])
        >>> state.blankLocation
        (1, 1)


        The blank is represented by a 0. state.cells is a 2-d array of numbers.
        """

        self.cells = cells
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == 0:
                    self.blankLocation = (i, j)
                    break

    def isGoal(self):

        """For the goal state, cells is equal to [[0, 1, 2], [3, 4, 5], [6, 7, 8]]"""
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] != 3*i + j:
                    return False

        return True 

    
    def getLegalMoves(self):

        """returns a list of legal moves available.
        >>> state = EightPuzzleState([[7, 2, 4], [5, 3, 1], [8, 0, 1]])
        >>> state.getLegalMoves()
        ['down', 'left', 'right'] """


        moves = []
        i, j = self.blankLocation
        if i != 2: moves.append('up')
        if i != 0: moves.append('down')
        if j != 2: moves.append('left')
        if j != 0: moves.append('right')

        return moves

    def getSuccessor(self, move):

        """takes a legal move as input and returns a new EightPuzzleState with that move applied."""

        newCells = [row.copy() for row in self.cells]
        i, j = self.blankLocation
        if move == 'up':
            newCells[i][j] = newCells[i+1][j]
            newCells[i+1][j] = 0
            return EightPuzzleState(newCells)

        if move == 'down':
            newCells[i][j] = newCells[i-1][j]
            newCells[i-1][j] = 0
            return EightPuzzleState(newCells)

        if move == 'left':
            newCells[i][j] = newCells[i][j+1]
            newCells[i][j+1] = 0
            return EightPuzzleState(newCells)

        if move == 'right':
            newCells[i][j] = newCells[i][j-1]
            newCells[i][j-1] = 0
            return EightPuzzleState(newCells)


    def __str__(self):

        """defines what happens when print() is called on an EightPuzzleState object."""

        boardString = '-------------\n'
        for i in range(3):
            boardString += '| '
            for j in range(3):
                char = str(self.cells[i][j]) if self.cells[i][j] != 0 else ' '
                boardString += char
                boardString += ' | '
            boardString += '\n-------------\n'
        return boardString

    def __hash__(self):

        """required for the closed set."""

        return hash(str(self.cells))

    def __eq__(self, other):

        """returns True if two EightPuzzleState objects represent the same board position. Required for the closed set."""

        for i in range(3):
            for j in range(3):
                if self.cells[i][j] != other.cells[i][j]:
                    return False
        return True
    


class EightPuzzleSearchProblem(SearchProblem):
    def __init__(self, cells):
        self.start = EightPuzzleState(cells)
    
    def getStartState(self):
        return self.start

    def isGoal(self, state):
        return state.isGoal()

    def getSuccessors(self, state):
        successors = []
        legalMoves = state.getLegalMoves()

        for move in legalMoves:
            successor = state.getSuccessor(move)
            successors.append((successor, move, 1))
        
        return successors

    def getCostOfActions(self, actions):
        return len(actions)

    def tilesHeuristic(self, state):

        """returns the number of misplaced tiles not counting the blank one."""


        count = 0
        for i in range(3):
            for j in range(3):
                if state.cells[i][j] != 0 and state.cells[i][j] != 3*i +j:
                    count +=1
        return count

    def manHattanHeuristic(self, state):

        """returns the sum of manhattan distance of every tile from where it should be. See slides."""

        distance = 0
        for i in range(3):
            for j in range(3):
                if state.cells[i][j] !=0:
                    correctRow, correctColumn = state.cells[i][j]//3, state.cells[i][j]%3
                    distance += abs(correctRow - i) + abs(correctColumn -j)
        return distance

    def showResults(self, actions):
        state = self.getStartState()
        print(state)
        for action in actions:
            state = state.getSuccessor(action)
            print(state)



def bfs(problem):

    """takes an instance of a SearchProblem as input, runs breadth-first search, and returns a list of actions""" 

    closed = set()
    fringe = Queue()
    numExpanded = 0
    fringe.push((problem.getStartState(), []))
    print(fringe)
    while not fringe.isEmpty():
        candidate, actions = fringe.pop()
        print(candidate, actions)
        if problem.isGoal(candidate):
            print('Number of expanded nodes: ' + str(numExpanded))
            print('Found solution with cost: ' + str(problem.getCostOfActions(actions)))
            return actions

        if candidate not in closed:

            closed.add(candidate)
            numExpanded += 1
            for successor, action, stepCost in problem.getSuccessors(candidate):
                newActions = actions.copy()
                fringe.push((successor, newActions+[action]))

    return None


def dfs(problem):
    """takes an instance of a SearchProblem as input, runs breadth-first search, and returns a list of actions"""

    closed = set()
    fringe = Queue()
    numExpanded = 0
    fringe.push((problem.getStartState(), []))
    print(fringe)
    while not fringe.isEmpty():
        candidate, actions = fringe.popright()
        if problem.isGoal(candidate):
            print('Number of expanded nodes: ' + str(numExpanded))
            print('Found solution with cost: ' + str(problem.getCostOfActions(actions)))
            return actions
        if candidate not in closed:
            closed.add(candidate)
            numExpanded += 1
            for successor, action, stepCost in problem.getSuccessors(candidate):
                newActions = actions.copy()
                fringe.push((successor, newActions+[action]))


def AStarSearch(problem, heuristic):
    closed = set()
    fringe = PriorityQueue()
    numExpanded = 0
    startState = problem.getStartState()
    fringe.push((startState, []), heuristic(startState))

    while not fringe.isEmpty():
        candidate, actions = fringe.pop()
        if problem.isGoal(candidate):
            print('Number of expanded nodes: ' + str(numExpanded))
            print('Found solution with cost: ' + str(problem.getCostOfActions(actions)))
            return actions
        if candidate not in closed:
            closed.add(candidate)
            numExpanded += 1
            for successor, action, stepCost in problem.getSuccessors(candidate):
                newActions = actions.copy()
                fringe.push((successor, newActions+[action]), problem.getCostOfActions(newActions) + stepCost + heuristic(successor))
    
    return None           

def ucs(problem):

    closed = set()
    fringe = PriorityQueue()
    numExpanded = 0
    startState = problem.getStartState()
    fringe.push((startState, []), 0)
    while not fringe.isEmpty():
        candidate, actions = fringe.pop()
        if problem.isGoal(candidate):
            print('Number of expanded nodes: ' + str(numExpanded))
            print('Found solution with cost: ' + str(problem.getCostOfActions(actions)))
            return actions
        if candidate not in closed:
            closed.add(candidate)
            for successor, action, stepCost in problem.getSuccessors(candidate):
                newActions = actions.copy()
                fringe.push((successor, newActions+[action]), problem.getCostOfActions(newActions) + stepCost + 0)


problem = EightPuzzleSearchProblem([[7, 2, 4], [5, 0, 6], [8, 3, 1]])
# actions = bfs(problem)
# print(actions)
# problem.showResults(actions)
# actions = AStarSearch(problem, problem.tilesHeuristic)
# problem.showResults(actions)
# actions = AStarSearch(problem, problem.manHattanHeuristic)
# problem.showResults(actions)
actions = ucs(problem)
problem.showResults(actions)