from pixel import pixel
import time, datetime
import os

#end = "2022-04-05 00:14:00.207"

def getFinal():
    base = "2022-04-01 23:26:51.728"
    pixels = []
    for filename in os.listdir("rplace"):
        with open(os.path.join("rplace", filename), 'r') as f:
            file = f.read().splitlines()
            for i, line in enumerate(file, 1):
                if i == 1:
                    continue
                line = line.replace('"', '')
                line = line.replace('UTC', '')
                x = line.split(',')

                if "2022-04-04 12:00:00.000" < x[0] < "2022-04-04 12:10:00.000":
                    pixels.append(line)

    return pixels


tps1 = time.clock()
if os.path.exists('final'):
    os.remove('final')
f = open("final", "a")
x = getFinal()
for l in x:
    f.write(l + "\n")
f.close()
tps2 = time.clock()
print(tps2 - tps1)
