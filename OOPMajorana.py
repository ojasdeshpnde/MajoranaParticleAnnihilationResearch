# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import math
import statistics
import numpy
import sys

class Particle:
    def __init__(self, position, id, pair, pairValue):
        self.position = position
        self.id = id
        self.pair = pair
        self.pairValue = pairValue

    def getPosition(self):
        return self.position

    def getId(self):
        return self.id

    def getPair(self):
        return self.pair

    def getPairValue(self):
        return self.pairValue

    def setPosition(self,pos):
        self.position = pos

    def setId(self,num):
        self.id = num

    def setPair(self,p):
        self.pair = p

    def setPairValue(self,p):
        self.pairValue = p


def checkPair(p,board,sign):
    pos = p.getPosition()
    if (board[pos+sign] == p.getPair()):
        return True
    else:
        return False






board = []
boardSize = 20
N0 = 10
particleList = []
counter = 1
for i in range(0,boardSize):
    if (i%(boardSize/N0)) == 0:
        board.append(counter)
        p = Particle(i,counter,-1, 1)
        counter = counter + 1
        particleList.append(p)
    else:
        board.append(0)
print(board)

for i in range(0,len(particleList)):
    if i % 2 == 0:
        p = particleList[i]
        p.setPair(p.getId()+1)
    else:
        p = particleList[i]
        p.setPair(p.getId()-1)

numParitcles = len(particleList)

x = random.randint(0,numParitcles-1)
p = particleList[x]
sign = 1
if random.random() < 0.5:
    sign = -1
while ((p.getPosition() == 0 and sign == -1) or (p.getPosition() == len(board) and sign == 1)):
    x = random.randint(0, numParitcles - 1)
    p = particleList[x]
    sign = 1
    if random.random() < 0.5:
        sign = -1
if board[p.getPosition()+sign] == 0:
    board[p.getPosition()+sign] = 1
    board[p.getPosition()] = 0
    p.setPosition(p.getPosition()+sign)
else:
    if checkPair(p,board,sign) == True:
        if p.getPairValue() == 0:
            del particleList[x]
            index = 0
            for i in range(0,len(particleList)):
                if particleList[i].getPosition() == p.getPosition()+sign:
                    index = i
            del particleList[index]
            board[p.getPosition()] = 0
            board[p.getPosition()+sign] = 0
    else:
        
