
""""
N-Queen problem
NxN chess board place N queens

Mutation function
Crossover Function
Fitness Function

"""
import random


class Board:

    def __init__(self, n):

        # board size or n
        self.size = n
        # max amount of clashes is sum of nums 1,2,3,4....
        self.fit = n * (n-1) / 2
        self.board = []
        for x in range(n):  # initialize positions
            self.board.append(random.randrange(n))
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
    size = len(parent1)
    splice1 = 


# def breed():

test = Board(4)
print(test.size)
print(test.fit)
print(test.board)