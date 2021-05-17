# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import matplotlib.pyplot as plt
import math



def sum(a):
    s = 0
    for i in range(0,len(a)):
        s = s + a[i]
    return s


board = []
location = []
numP = []

for i in range(0,1000):
    board.append(0)
for i in range(0,200):
    x = random.randint(0,999)
    while(x in location):
        x = random.randint(0,999)
    location.append(x)
    board[x] = 1
counter = 0
numParticles = sum(board)
while (numParticles > 0 and counter < 1000000):
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

    if board[pos + sign] == 1:
        if (random.random() < 1):
            board[pos] =0
            board[pos+sign] = 0
            del location[x]
            del location[location.index(pos+sign)]
            numParticles = sum(board)
    else:
        board[pos] = 0
        board[pos+sign] = 1
        del location[x]
        location.append(pos+sign)
        numParticles = sum(board)
    numP.append(numParticles/1000)
    counter = counter + 1
    print(counter)

time = []
for i in range(0,len(numP)):
    time.append(i)

y = []
y.append(1/(math.sqrt(4*(math.pi)*1)))
for i in range(1,len(time)):
    y.append(1/(math.sqrt(4*(math.pi)*time[i])))


plt.plot(time, y)
plt.plot(time,numP)
plt.xlabel('Time')
plt.ylabel('Number of Particles')
plt.show()