Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
... points = [(1, 2), (4, 6), (7, 8), (2, 1)]
... 
... def euclideanDistance(point1, point2):
...     return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
... distances = []
... for i in range(len(points)):
...     for j in range(i + 1, len(points)):
...         distance = euclideanDistance(points[i], points[j])
...         distances.append(distance)
... min_distance = min(distances)
