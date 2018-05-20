
""""
N-Queen problem
NxN chess board place N queens

Mutation function
Crossover Function
Fitness Function

"""
import random


class Board:
    size = 0
    board = []
    fit = 0

    def __init__(self, n):

        # board size or n
        self.size = n
        # max amount of clashes is n * n-1, 3 queens in a row = 2 + 2 + 2
        self.fit = n * (n-1)
        for x in range(n):  # initialize positions
            self.board[x] = random.randrange(n-1)


# def mutation():

# def crossover():


def fitness(board):
    # calculate by amount of clashes
    board.board


# def breed():

Board(8)
print(Board.size)
