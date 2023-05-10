from queue import Queue
from elements.ponto import Ponto
from elements.envoltoria import *
from elements.poligono import Poligono
from elements.ponto import Ponto
from pprint import pprint

# MAKES A BREADTH FISRT SEARCH TO FIND THE OBJECTS
def bfs_objects(img, x, y, visited):

    q = Queue()
    q.put((x, y))

    obj = set()

    while not q.empty():

        x, y = q.get()
        m, n = img.shape[0], img.shape[1]

        if (x >= 0 and x < m and y >= 0 and y < n and not visited[x][y]):

            if img[x][y] == 1:

                visited[x][y] = True
                
                obj.add((x,y))

                q.put((x-1, y-1))
                q.put((x, y-1))
                q.put((x+1, y-1))
                q.put((x-1, y))
                q.put((x+1, y))
                q.put((x-1, y+1))
                q.put((x, y+1))
                q.put((x+1, y+1))

    return obj

# MAKES A BREADTH FISRT SEARCH TO FIND THE OBJECTS
def bfs_holes(img, x, y, visited):

    q = Queue()

    q.put((x, y))

    hole = set()

    while not q.empty():

        x, y = q.get()
        m, n = img.shape[0], img.shape[1]

        if (x >= 0 and x < m and y >= 0 and y < n and not visited[x][y]):

            if img[x][y] == 0:

                visited[x][y] = True

                hole.add((x,y))

                q.put((x, y-1))
                q.put((x-1, y))
                q.put((x+1, y))
                q.put((x, y+1))

    return hole

# CHECK IF POINT IS IN THE BORDER
def is_in_border(x, y, img):

    m, n = len(img)-1, len(img[0])-1

    return ( x == 0 ) or ( y == 0 ) or (x == m) or (y == n)

# COUNTS HOW MANY SETS OF POINTS (equal to 0) ARE FOUND IN THE SEARCH
def count_objects(img):

    visited = np.zeros(img.shape[:2], dtype=bool)
    m, n = img.shape[0], img.shape[1]

    obj_counter = 0
    
    for x in range(m):
        for y in range(n):
            if not visited[x][y] and img[x][y] == 1:
                bfs_objects(img, x, y, visited)
                obj_counter += 1

    return obj_counter

# COUNTS HOW MANY SETS OF POINTS (equal to 0) ARE FOUND IN THE SEARCH
def count_holes(img):

    visited = np.zeros(img.shape[:2], dtype=bool)
    m, n = img.shape[0], img.shape[1]

    hole_counter = 0

    for i in range(m):
        for j in range(n):
            if not visited[i][j] and img[i][j] == 0 and not is_in_border(i, j, img):
                hole = bfs_holes(img, i, j, visited)
                if any([is_in_border(pixel[0], pixel[1], img) for pixel in hole]):
                    continue
                hole_counter += 1
                
    return hole_counter

# RETURNS A LIST OF THE SETS OF POINTS THE COMPOUND EACH OBJECT
def return_objects(img):

    visited = np.zeros(img.shape[:2], dtype=bool)
    m, n = img.shape[0], img.shape[1]

    objects = []

    for x in range(m):
        for y in range(n):
            if not visited[x][y] and img[x][y] == 1:
                obj = bfs_objects(img, x, y, visited)
                objects.append(obj)

    return objects

# RETURNS A LIST OF THE SETS OF POINTS THE COMPOUND EACH HOLE
def return_holes(img):

    visited = np.zeros(img.shape[:2], dtype=bool)
    m, n = img.shape[0], img.shape[1]

    holes = []

    for i in range(m):
        for j in range(n):
            if not visited[i][j] and img[i][j] == 0 and not is_in_border(i, j, img):
                hole = bfs_holes(img, i, j, visited)
                if any([is_in_border(pixel[0], pixel[1], img) for pixel in hole]):
                    continue
                holes.append(hole)
                
    return holes

# FOR EVERY OBJECT AND HOLE FOUND, CHECKS IF A POINT CONTAINED IN THE HOLE SET IS INSIDE THE POLIGON
# DEFINED BY THE CONVEX HULL OF THE OBJECT
def count_object_with_holes(objects, holes):
    c = 0 
    for obj in objects:
        #print(len(obj))
        if len(obj) >= 3:
            hull = Jarvis([Ponto(x,y) for x,y in obj])              # RETURNS THE CONVEX HULL

            poligono = Poligono(hull)                               # CREATES A REGULAR POLIGON
            check = []
            for hole in holes:                                      
                p = next(iter(hole))                                # TAKES A POINT FROM THE HOLE SET
                check.append(poligono.contem(Ponto(p[0], p[1])))    # CHECK IF THE POINT IS INSIDE THE POLIGON
            if any(check):                                          # IF SOME HOLE IS INSIDE THE POLIGON, INCREMENTS THE COUNTER
                c += 1

    return c


if __name__=="__main__":

    import os
    import numpy as np
    
    path = str(__file__)
    i = path.rfind(os.path.sep)
    
    os.chdir(path[:i])

    while 1:
        
        arquivo = input("\nDigite o nome do arquivo (sem extensão): ")

        with open(f"images/{arquivo}.pbm", 'r') as f:
            
            img = np.array([list(map(int, line.strip().split())) for line in f.readlines()[2:]])

            obj_counter = count_objects(img)
            hole_counter = count_holes(img)

            objects = return_objects(img)
            holes = return_holes(img)

            obj_with_holes_counter = count_object_with_holes(objects, holes)
            
            print(f'Image: {arquivo}.pbm')
            print("Number of objects:", obj_counter)
            print("Number of holes:", hole_counter)
            print("Number of objects with holes:", obj_with_holes_counter)
            print("Number of objects without holes:", obj_counter - obj_with_holes_counter)
    
"""
    files = [ f.split(".")[0] for f in os.listdir('C:/Users/55799/Desktop/PI/images') if 'pbm' in f]
    for i in files:
        with open(f"images/{i}.pbm", "r") as f:
            img = np.array([list(map(int, line.strip().split())) for line in f.readlines()[2:]])
        
        obj_counter = count_objects(img)
        hole_counter = count_holes(img)

        objects = return_objects(img)
        holes = return_holes(img)

        obj_with_holes_counter = count_object_with_holes(objects, holes)
        
        print('\n'+i+':')
        print("Number of objects:", obj_counter)
        print("Number of holes:", hole_counter)
        print("Number of objects with holes:", obj_with_holes_counter)
        print("Number of objects without holes:", obj_counter - obj_with_holes_counter)

"""