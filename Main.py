
""""
N-Queen problem
NxN chess board place N queens

Mutation function
Crossover Function
Fitness Function

"""
import random

SIZE = 16
POPULATION = 10
ANSWER = False
SOLUTION = []
MAXFIT = SIZE*(SIZE-1)/2


class Board:

    def __init__(self, n, new=None):

        # board size or n
        self.size = n
        # max amount of clashes is sum of nums 1,2,3,4....
        self.fit = n * (n-1) / 2
        if new is None:
            self.board = []
            for x in range(n):  # initialize positions
                self.board.append(random.randrange(n))
            self.fitness()
        else:
            self.board = new
            self.fitness()

    # uses slope to find diagonals
    def fitness(self):
        size = len(self.board)
        fit = self.fit
        for x in range(size):
            queen1 = self.board[x]
            for y in range(x+1, size):
                queen2 = self.board[y]
                xslope = y - x
                yslope = queen2 - queen1
                slope = yslope/xslope
                if queen1 == queen2:
                    fit = fit - 1
                if slope == 1:
                    fit = fit - 1
                elif slope == -1:
                    fit = fit - 1
        self.fit = fit


# changes on random gene
def mutation(child):
    index = random.randrange(SIZE)
    gene = random.randrange(SIZE)
    # print(index, gene)
    child.board[index] = gene


def crossover(parent1, parent2):
    global ANSWER
    global SOLUTION
    # just going to divide parents in half
    splice1 = parent1[:len(parent1)//2]
    splice2 = parent1[len(parent1)//2:]
    splice3 = parent2[:len(parent2)//2]
    splice4 = parent2[len(parent2)//2:]

    child = splice1 + splice4
    child1 = Board(SIZE, child)
    # print(child1.board, "child 1", child1.fit)
    childother = splice3 + splice2
    child2 = Board(SIZE, childother)
    # print(child2.board, "child 2", child2.fit)

    if child1.fit == MAXFIT:
        ANSWER = True
        SOLUTION = child1.board
    elif child2 == MAXFIT:
        ANSWER = True
        SOLUTION = child2.board

    return child1, child2


def selection(gen):
    global SOLUTION
    global ANSWER
    pop = len(gen)
    rand = random.randrange(pop)
    fittest = gen[0]
    ideal = (SIZE-1)*SIZE/2
    fitter = gen[rand]
    most = fittest.fit
    weaker = fitter.fit
    dead = []
    for x in range(9):
        if most > weaker:
            rand = random.randrange(pop)
            if fitter not in dead:
                dead.append(fitter)
            fitter = gen[rand]
            while fitter in dead:
                rand = (rand + 1) % pop
                fitter = gen[rand]
            weaker = fitter.fit
        elif most == ideal == weaker:
            SOLUTION = fittest.board
            ANSWER = True
            return fittest, fitter
        else:
            rand = random.randrange(pop)
            if fittest not in dead:
                dead.append(fittest)
            fittest = gen[rand]
            while fittest in dead:
                rand = (rand + 1) % pop
                fittest = gen[rand]
            most = fittest.fit
        # print(fittest.board, fitter.board)
    return fittest, fitter


# test = Board(SIZE)
# print(test.size)
# print(test.fit)
    # print(test.board)

gen = []
children = []
average = []
x = 0
for y in range(POPULATION):
    gen.append(Board(SIZE))
while ANSWER is False:
    total = 0
    if x == 0:
        for z in range(POPULATION//2):
            parent1, parent2 = selection(gen)
            child1, child2 = crossover(parent1.board, parent2.board)
            children.append(child1)
            children.append(child2)
            total += child1.fit
            total += child2.fit
        print(total, "i am total")
        average.append(total/POPULATION)
        gen = children
    else:
        for y in range(POPULATION//2):
            parent1, parent2 = selection(gen)
            child1, child2 = crossover(parent1.board, parent2.board)
            children[y] = child1
            children[POPULATION-y-1] = child2
            total += child1.fit
            total += child2.fit
        average.append(total / POPULATION)
        mutant = children[random.randrange(POPULATION)]
        mutation(mutant)
        gen = children
    x += 1
    print(x)

print(SIZE, MAXFIT, SOLUTION, x, average)
