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


def boardPrint(board):
    print("[", end = '')
    for i in range(0,len(board)):
        if board[i] != 0:
            print("1", end = '')
        else:
            print("0", end='')
        if i != len(board) -1:
            print(",", end = '')
    print("]", end = '')


total = []
for k in range(0,100):
    print(k)
    numP = []
    board = []
    boardSize = 10
    N0 = 2
    particleList = []
    counter = 1
    for i in range(0,boardSize):
        if (i%(boardSize/N0)) == 0:
            p = Particle(i,counter,None, 1)
            board.append(p)
            counter = counter + 1
            particleList.append(p)
        else:
            board.append(0)
    print(board)

    for i in range(0,len(particleList)):
        if i % 2 == 0:
            p = particleList[i]
            p.setPair(particleList[i+1])
        else:
            p = particleList[i]
            p.setPair(particleList[i-1])
    for j in range(0,1000):
        numParticles = len(particleList)
        numP.append(numParticles/len(board))
        for i in range(0,numParticles):
            x = random.randint(0,len(particleList)-1)
            p = particleList[x]
            sign = 1
            if random.random() < 0.5:
                sign = -1
            while ((p.getPosition() == 0 and sign == -1) or (p.getPosition() == len(board)-1 and sign == 1)):
                x = random.randint(0, len(particleList) - 1)
                p = particleList[x]
                sign = 1
                if random.random() < 0.5:
                    sign = -1
            if board[p.getPosition()+sign] == 0:
                board[p.getPosition()+sign] = board[p.getPosition()]
                board[p.getPosition()] = 0
                p.setPosition(p.getPosition()+sign)
            else:
                if p.getPair() == board[p.getPosition() + sign]:
                    if p.getPairValue() == 0:
                        particleList.remove(p)
                        particleList.remove(board[p.getPosition()+sign])
                        board[p.getPosition()] = 0
                        board[p.getPosition()+sign] = 0
                        # if p.getPairValue() == 1 then do nothing since they are already paired
                else:
                    s = p.getPair()
                    q = board[p.getPosition()+sign]

                    r = q.getPair()
                    n = p.getPairValue()
                    nPrime = q.getPairValue()
                    m = 0
                    if random.random() < 0.5:
                        m = 1
                    mPrime = 0
                    if ((n+nPrime) % 2 != (m + mPrime) %2):
                        mPrime = 1

                    p.setPair(q)
                    q.setPair(p)
                    p.setPairValue(m)
                    q.setPairValue(p.getPairValue())

                    s.setPair(r)
                    r.setPair(s)
                    s.setPairValue(mPrime)
                    r.setPairValue(s.getPairValue())
                    if m == 0:
                        particleList.remove(p)
                        particleList.remove(q)
                        board[p.getPosition()] = 0
                        board[q.getPosition()] = 0
    total.append(numP)

average = []
totalStd = []
for i in range(0,len(total[0])):
    sum = 0
    temp = []
    for j in range(0,len(total)):
        sum = sum + total[j][i]
        temp.append(total[j][i])
    average.append(sum/len(total))
    totalStd.append(statistics.stdev(temp))


time = []
for i in range(0,len(numP)):
    time.append(i)


y = []
y.append(1/(math.sqrt(4*(math.pi)*1)))
for i in range(1,len(time)):
    y.append(1/(math.sqrt(4*(math.pi)*time[i])))

plt.yscale("log")
plt.xscale("log")
plt.plot(time, y)
plt.plot(time,average)
plt.xlabel('Time')
plt.ylabel('Particle Density')
plt.show()