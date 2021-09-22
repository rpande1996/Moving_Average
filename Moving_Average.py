import matplotlib.pyplot as plt
import statistics

x = []
y = []
xmavg = []

with open('imudata.txt', 'r') as f:
    data = f.read().split('\n')
    for elem in data:
        elem = elem.split(' ')
        try:
            y.append(int(elem[4]))
        except (ValueError, IndexError):
            pass

x = list(range(len(y)))

size = int(input("Enter the desired point moving average: "))
i = 0
mavg = []
while i < len(y) - size + 1:
    win = y[i: i + size]
    wavg = sum(win)/size
    mavg.append(wavg)
    i = i + 1

xmavg = list(range(len(mavg)))
mn = statistics.mean(mavg)
sd = statistics.stdev(mavg)

xline = [min(x), max(x)]
mnline = [mn, mn]
psdline = [mn+sd, mn+sd]
nsdline = [mn-sd, mn-sd]

plt.plot(x, y)
plt.plot(xmavg, mavg)
plt.plot(xline, mnline, color='black')
plt.plot(xline, psdline, linestyle='--', color='black')
plt.plot(xline, nsdline, linestyle='--', color='black')
plt.text(300, 15.5, f'Mean is {"%.2f" % mn}')
plt.text(300, 15, f'SD is ± {"%.2f" % sd}')
plt.xlabel('Reading Number')
plt.ylabel('Rotation in degrees')
plt.title('Sensor Data')
plt.legend(['Raw Data', f'{size} point Moving Average', 'Mean', 'Standard Deviation'])
plt.show()
