# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import matplotlib.pyplot as plt
import math


board = []
location = []
numP = []
finP = []

p = 0.5

for i in range(0,1000):
    board.append(0)
for i in range(0,200):
    x = random.randint(0,len(board)-1)
    while(x in location):
        x = random.randint(0,999)
    location.append(x)
    board[x] = 1

numParticles = len(location)
counter = 0

while (numParticles > 0 and counter < 100000):

    x = random.randint(0,len(location)-1)
    pos = location[x]

    sign = 1
    while(random.random() < 0.5):
        sign = -1

    while((pos == 0 and sign == -1) or (pos == len(board)-1 and sign == 1)):

        x = random.randint(0, len(location) - 1)
        pos = location[x]

        sign = 1
        while (random.random() < 0.5):
            sign = -1
    if board[pos + sign] == 0:
        board[pos] = 0
        board[pos + sign] = 1
        del location[x]
        location.append(pos+sign)
    for i in range(0, len(board)-1):
        if random.random() < p:
            if (board[i] == 1 and board[i+1] == 1):
                board[i] = 0
                board[i+1] = 0
                del location[location.index(i)]
                del location[location.index(i+1)]
    numParticles = len(location)
    numP.append(numParticles/1000)
    counter = counter + 1
time = []
for i in range(0,len(numP)):
    if i % 200 == 0:
        finP.append(numP[i])

for i in range(0,len(finP)):
    time.append(i)

y = []
y.append(1/(math.sqrt(4*(math.pi)*1)))
for i in range(1,len(time)):
    y.append(1/(math.sqrt(4*(math.pi)*time[i])))

plt.yscale("log")
plt.xscale("log")
plt.plot(time, y)
plt.plot(time,finP)
plt.xlabel('Time')
plt.ylabel('Particle Density')
plt.show()

