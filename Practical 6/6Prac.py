import random
import math

data = []
for i in range(20):
    x = random.randint(0, 50)
    y = random.randint(0, 50)
    if x < 26 or y < 26:
        label = 1
    else:
        label = -1
    data.append((x, y, label))

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def find_neighbors(data, point, k):
    distances = []
    for x, y, label in data:
        dist = euclidean_distance((x, y), point)
        distances.append((dist, label))
    distances.sort()
    neighbors = [label for dist, label in distances[:k]]
    return neighbors

def classify(data, point, k):
    neighbors = find_neighbors(data, point, k)
    positive = sum(1 for label in neighbors if label == 1)
    negative = sum(1 for label in neighbors if label == -1)
    if positive > negative:
        return 1
    else:
        return -1

for k in range(1,6):
    print(f"Classification results for k={k}:")
    for x, y, label in data:
        predicted_label = classify(data, (x, y), k)
        print(f"Data point ({x}, {y}) with actual label {label} was classified as {predicted_label}")