import random

class Game:
    def __init__(self,id):
        self.id=id
        self.points=[]
        self.max=0

    def minimax(self,depth, nodeIndex, maximizingPlayer,
                values, alpha, beta):
        MIN,MAX=-1000,1000
        if depth == 3:
            return values[nodeIndex]
        if maximizingPlayer:
            best = MIN
            for i in range(0, 2):
                val = self.minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return best
        else:
            best = MAX
            for i in range(0, 2):
                val = self.minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
            return best

    def point_to_win(self):
        self.need = int(self.id[-1:-3:-1])
        return self.need


    def max_lim(self):

        self.max = int(self.id[-1:-3:-1])*1.5
        if self.max-int(self.max)!=0.0:
            self.max=int(self.max)+1
        return int(self.max)

    def point_generator(self):
        self.min = int(self.id[4])
        for i in range (0,8):
            n=random.randrange(self.min,self.max_lim())
            self.points.append(n)
        return self.points

    def winner(self,point):
        if point>self.need:
            return "The winner is Optimus Prime"
        else:
            return "The winner is Megatron"


    def shuffle(self,arr):
        self.new_arr=arr
        random.shuffle(self.new_arr)
        return self.new_arr


st_id=input("Enter your ID: ")
a=Game(st_id)
values = a.point_generator()
point=a.minimax(0, 0, True, values, -1000, 1000)
print("Generated 8 random points between the minimum and maximum point limits: ",values)
print("Total points to win:",a.point_to_win())
print("Achieved point by applying alpha-beta pruning = ",a.minimax(0, 0, True, values, -1000, 1000))
print(a.winner(point))

print("======================================================")
print("After the shuffle:")


#Task-2
num_of_shuffle=int(st_id[3])
best_vals=[]
for i in range(0,num_of_shuffle):
    array=a.shuffle(values)
    besst=a.minimax(0, 0, True, array, -1000, 1000)
    best_vals.append(besst)

print("List of all points values from each shuffle:",best_vals)
print("The maximum value of all shuffles: ", max(best_vals))
count=0
for i in best_vals:
    winner=a.winner(i)
    if winner=="The winner is Optimus Prime":
        count+=1
print("Won",count,"Times out of ",len(best_vals),"numbers of shuffles")