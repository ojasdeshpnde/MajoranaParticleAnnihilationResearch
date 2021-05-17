# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import math
import statistics





temp = []
sum = []
p = 0.5



for i in range(0,100):
    sum.append(0)

for k in range(0,100):
    print(k)
    board = []
    location = []
    numP = []
    for i in range(0, 1000):
        board.append(0)
    for i in range(0, 200):
        x = random.randint(0, len(board) - 1)
        while (x in location):
            x = random.randint(0, 999)
        location.append(x)
        board[x] = 1

    for i in range(0,100):
        numParticles = len(location)
        numP.append(numParticles/1000)
        for j in range(0,numParticles):
            if len(location) != 0:
                x = random.randint(0, len(location) - 1)
                pos = location[x]

                sign = 1
                while (random.random() < 0.5):
                    sign = -1

                while ((pos == 0 and sign == -1) or (pos == len(board) - 1 and sign == 1)):

                    x = random.randint(0, len(location) - 1)
                    pos = location[x]

                    sign = 1
                    while (random.random() < 0.5):
                        sign = -1
                if board[pos + sign] == 0:
                    board[pos] = 0
                    board[pos + sign] = 1
                    del location[x]
                    location.append(pos + sign)
                else:
                    if random.random() < p:
                        board[pos] = 0
                        board[pos+sign] = 0
                        del location[x]
                        del location[location.index(pos+sign)]
    for i in range(0,len(numP)):
        temp.append(sum[i] + numP[i])
    sum = temp.copy()
    temp.clear()

average = []
for i in range(0,len(sum)):
    average.append(sum[i]/100)

time = []


for i in range(0,len(numP)):
    time.append(i)

y = []
y.append(1/(math.sqrt(4*(math.pi)*1)))
for i in range(1,len(time)):
    y.append(1/(math.sqrt(4*(math.pi)*time[i])))

s = statistics.stdev(average)
error = s / math.sqrt(100)






plt.plot(time, y)
plt.plot(time,average)
plt.xlabel('Time')
plt.ylabel('Particle Density')
plt.errorbar(time, average, yerr = 2*error, fmt = "o",color="b")
plt.show()
