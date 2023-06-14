import math

while True:
    line = input()
    if not line:
        break
    x1, y1, x2, y2 = map(int, line.split())
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(distance)
