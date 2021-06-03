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
    def __init__(self, position, pair, pairValue):
        self.position = position
        self.pair = pair
        self.pairValue = pairValue

    def getPosition(self):
        return self.position


    def getPair(self):
        return self.pair

    def getPairValue(self):
        return self.pairValue

    def setPosition(self,pos):
        self.position = pos

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
    print(k+1)
    numP = []
    board = []
    boardSize = 1000
    N0 = 500
    particleList = []
    counter = 1
    for i in range(0,boardSize):
        board.append(0)
    occupied = []
    for i in range(0,N0):
        x = random.randint(0,len(board)-1)
        while x in occupied:
            x = random.randint(0,len(board)-1)
        occupied.append(x)
        p = Particle(x,None, 1)
        board[x] = p
        particleList.append(p)


    v = False
    a = 0
    b = 0
    for i in range(0,len(board)):
        if board[i] != 0:
            if v == False:
                a = i
                v = True
            else:
                b = i
                v = False
                board[a].setPair(board[b])
                board[b].setPair(board[a])
                a = 0
                b = 0

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
    totalStd.append(1*(statistics.stdev(temp)/math.sqrt(100)))


time = []
for i in range(0,len(numP)):
    time.append(i)


y = []
y.append(2/(math.sqrt(4*(math.pi)*1)))
for i in range(1,len(time)):
    y.append(2/(math.sqrt(4*(math.pi)*time[i])))

plt.yscale("log")
plt.xscale("log")
plt.plot(time, y)
plt.plot(time,average)
plt.xlabel('Time')
plt.ylabel('Particle Density')
# plt.errorbar(time, average, yerr = totalStd, fmt = "o",color="b")
plt.show()