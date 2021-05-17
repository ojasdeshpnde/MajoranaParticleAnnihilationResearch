# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import matplotlib.pyplot as plt
import math

def add(a,b):
    k = []

def sum(a):
    s = 0
    for i in range(0,len(a)):
        s = s + a[i]
    return s

board = []
location = []
numP = []
finP = []

for i in range(0,1000):
    if i % 5 == 0:
        board.append(1)
        location.append(i)
    else:
        board.append(0)

numParticles = sum(board)
counter = 0

while (numParticles > 0 and counter < 100000):
    sign = 1
    if random.random() < 0.5:
        sign = -1
    x = random.randint(0,numParticles-1)
    pos = location[x]
    while (pos==0 and sign == -1) or (pos == (len(board)-1) and sign == 1):
        sign = 1
        if random.random() < 0.5:
            sign = -1
        x = random.randint(0, numParticles - 1)
        pos = location[x]
    if board[pos+sign] == 0:
        board[pos] = 0
        board[pos+sign] = 1
        del location[x]
        location.append(pos+sign)

    for i in range(0,len(board)-1):
        if board[i] == 1 and board[i+1] == 1 and random.random() < 0.5:
            board[i] = 0
            board[i+1] = 0
            del location[location.index(i)]
            del location[location.index(i+1)]

    numParticles = sum(board)
    numP.append(numParticles / 1000)
    counter = counter + 1

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
plt.plot(time,numP)
plt.xlabel('Time')
plt.ylabel('Particle Density')
plt.show()

