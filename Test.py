from Delaunator import *

points = [[382, 302], [382, 328], [382, 205], [623, 175], [382, 188], [382, 284], [623, 87], [623, 341], [141, 227]]

triangles = Delaunator().run(points)
print(triangles)
