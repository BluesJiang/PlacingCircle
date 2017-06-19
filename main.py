


import math
import numpy as np
#from matplotlib import pyplot as plt
from tkinter import * 
from pprint import pprint
import random
import time
from datetime import datetime
radius_sum = 0
class Circle():
    center = (0, 0) 
    radius = 0
    def __init__(self, center=(0,0), radius=0):
        self.center = center
        self.radius = radius

    def calAria(self):
        return math.pi*self.radius*self.radius
    
    def description(self):
        return ("Center: (% f, % f)\tRadius:%.10f"%(self.center[0], self.center[1], self.radius))

    def distance(circle1, circle2=None, point=None):
        if circle2 != None:
            return math.sqrt((circle1.center[0]-circle2.center[0])**2+(circle1.center[1]-circle2.center[1])**2)
        elif point != None:
            return math.sqrt((circle1.center[0]-point[0])**2+(circle1.center[1]-point[1])**2)
        return 0

    def overlap(circle1, circle2=None, point=None):
        if circle2 != None:
            return Circle.distance(circle1, circle2) < (circle1.radius+circle2.radius)
        elif point != None:
            return Circle.distance(circle1, point=point) < circle1.radius
        return False
    
    def copy(self):
        return Circle(self.center, self.radius)


def valid(circle, circleList):
    
    if abs(circle.center[0]) + circle.radius > 1 or abs(circle.center[1]) + circle.radius > 1 :
        return False
    
    for tmpCircle in circleList:
        if(Circle.distance(tmpCircle, circle) < tmpCircle.radius + circle.radius):
            return False
    return True

def maxValidRadius(center, circleList):
    res = 0
    res = min(map(math.fabs,[center[0]+1, center[0]-1, center[1]+1, center[1]-1]))
    for circle in circleList:
        dis = Circle.distance(circle, point=center) - circle.radius
        if dis < res:
            res = dis
    return res

def sub_solution_r(m):
    circles = []
    R = [1]
    circles.append(Circle(radius=1))
    sym_x = [1, 1, -1, -1]
    sym_y = [1, -1, 1, -1]
    if m == 0:
        return []
    if m == 1:
        return circles
    if m > 1:
        R1 = 3 - 2 * math.sqrt(2)
        R.append(R1)
        y = x = 1 - R1
        for i in range(0, 4):
            circles.append(Circle((x * sym_x[i], y * sym_y[i]), R1))
            if len(circles) == m:
                break
    if m > 5:
        pend_height = 0
        k = m - 5
        if k % 8 == 0:
            k = int(k / 8)
        else:
            k = int(k / 8) + 1
        pend_current = R[1]
        for i in range(1, k+1): 
            r = ((1 - pend_current)/ (2 * (1+math.sqrt(R[i])))) ** 2
            pend_current += 2 * math.sqrt(r * R[i])
            R.append(r)
            x = 1 - r
            y = 1 - pend_current
            for j in range(4):
                circles.append(Circle((x * sym_x[j], y * sym_y[j]), r))
                if len(circles) == m:
                    break
                circles.append(Circle((y * sym_y[j], x * sym_x[j]), r))
                if len(circles) == m:
                    break
    return circles
                


def mathmatic_solution(m, pointList, circleList = []):
    radius_sum = 0
    center_step = 0.01
    for i in range(0, m):
        maxcircle = Circle()
        circle = 0
        for point in pointList:
            circle = Circle(point, maxValidRadius(point, circleList))
            # radius_step = 0.1
            # while radius_step > 1e-5:
            if circle.radius > maxcircle.radius:
                maxcircle = circle.copy()
            #     circle.radius += radius_step
            #     if not valid(circle, circleList):
            #         circle.radius -= radius_step
            #         radius_step /= 2

        # if valid(maxcircle, circleList):
        circleList.append(maxcircle)
        # radius_sum += maxcircle.radius**2
        # pointList = list(filter(lambda point: valid(Circle(point, 0), circleList) ,pointList))
        pointList = list(filter(lambda point: Circle.distance(maxcircle, point=point) > maxcircle.radius , pointList))

    return circleList

def main():
    random.seed(time.time())
    rate = []
    X = np.linspace(-1, 1, 201)
    pointList = []
    for i in X:
        for j in X:
            pointList.append((i,j))
    circleList = []
    for i in range(4):
        point = (random.uniform(-1,1), random.uniform(-1,1), 0)
        circleList.append(Circle(point))
    #for m in range(0, 100):
    start = datetime.now().timestamp()
    circles = mathmatic_solution(30, pointList, circleList)
    # circles = sub_solution_r(100)
    end = datetime.now().timestamp()
    print("gap:"+str(end-start))
    # pprint(list(map(Circle.description, circles)))
    #     total = sum([cir.calAria() for cir in circles ])
    #     rate.append(total/4*100)
    # m = np.linspace(0,99,100)
    # print(m)
    #print(m)
    # print(rate)
    
    root = Tk()
    root.title("Circle with pins")
    w = Canvas(
           root,
           width = 800,
           height = 800,
           background="white"
          )
    w.pack()
    w.create_rectangle(100, 100, 700, 700, outline = "black")
    i = 0
    for circle in circles:
        fill = "gray"
        outline = "black"
        if i < 0:
            circle.radius = 0.01
            outline = "red"
            fill = "red"
        point1 = circle.center[0] - circle.radius
        point2 = circle.center[1] - circle.radius
        point3 = circle.center[0] + circle.radius
        point4 = circle.center[1] + circle.radius
        w.create_oval(400 + 300 * point1, 400 + 300 * point2, 400 + 300 * point3, 400 + 300 * point4, fill = fill, outline=outline)
        i += 1
    mainloop()
    

if __name__ == '__main__':
    main()