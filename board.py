#import numpy as np
from tiles import *
import csv
class Board:
    size = 16
    
    #goals should be an array of 2, containing x and y
    def __init__(self, filename):
        self.filename = filename
        #self.goals = goals
        #self.verticalWalls = np.array([[0 for _ in range(15)] for _ in range(15)])
        #self.horizontalWalls = np.array([[0 for _ in range(15)] for _ in range(15)])
    
    def getTile(self, x, y):
        return self.matrix[y][x]

    #Get a Row from game board (only need where 1s and 3s are)
    def getRow(self, row):
        row = self.matrix[row]
        return [0 if (x==2 | x==0) else 1 for x in row]

    #Get a column from game board (only need where 2s and 3s are)
    def getCol(self, col):
        col = [row[col] for row in self.matrix]
        return [0 if (x==1 | x==0) else 1 for x in col]
    
    
    def read_csv(self):
        matrix = []
        with open(os.path.join(self.filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                matrix.append(list(row))
        return matrix

    #creates a board (currently one board)
    #TODO: generate boards from 4 tiles

    
    


        











