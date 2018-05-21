
""""
N-Queen problem
NxN chess board place N queens

Mutation function
Crossover Function
Fitness Function

"""
import random

SIZE = 4


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


# def mutation():


def crossover(parent1, parent2):
    # just going to divide parents in half
    splice1 = parent1[:len(parent1)//2]
    splice2 = parent1[len(parent1)//2:]
    splice3 = parent2[:len(parent2)//2]
    splice4 = parent2[len(parent2)//2:]

    child = splice1 + splice4
    child1 = Board(SIZE, child)
    print(child1.board, "child 1", child1.fit)
    childother = splice3 + splice2
    child2 = Board(SIZE, childother)
    print(child2.board, "child 2", child2.fit)

    return child1, child2


test = Board(SIZE)
# print(test.size)
# print(test.fit)
# print(test.board)
gen = []
for x in range(2):
    gen.append(Board(SIZE))
    print(gen[x].board)

childtest, childtwo = crossover(gen[0].board, gen[1].board)
# print(childtest.board, childtest.fit, childtwo.board, childtwo.fit)
