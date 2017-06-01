


import math
import numpy as np
from pprint import pprint
from matplotlib import pyplot as plt


radius_sum = 0
class Circle():
    center = (0, 0) 
    radius = 0
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def calAria(self):
        return math.pi*self.radius*self.radius
    
    def description(self):
        return ("Center: (% f, % f)\tRadius:%.10f"%(self.center[0], self.center[1], self.radius))

    def distance(circle1, circle2):
        return math.sqrt((circle1.center[0]-circle2.center[0])**2+(circle1.center[1]-circle2.center[1])**2)
    def copy(self):
        return Circle(self.center, self.radius)


def valid(circle, circleList):
    
    if abs(circle.center[0]) + circle.radius > 1 or abs(circle.center[1]) + circle.radius > 1 :
        return False
    
    for tmpCircle in circleList:
        if(Circle.distance(tmpCircle, circle) < tmpCircle.radius + circle.radius):
            return False
    return True




def sub_solution_r(m):
    circles = []
    R = [1]
    circles.append(Circle((0, 0), 1))
    sym_x = [1, 1, -1, -1]
    sym_y = [1, -1, 1, -1]
    if m == 0:
        return []
    if m == 1:
        return circles
    elif m <= 5:
        r = 3 - 2 * math.sqrt(2)
        y = x = 1 - r
        for i in range(0, 4):
            circles.append(Circle((x * sym_x[i], y * sym_y[i]), r))
            if len(circles) == m:
                break
        return circles
    elif m > 5:
        R1 = 3 - 2 * math.sqrt(2)
        R.append(R1)
        y = x = 1 - R1
        for i in range(0, 4):
            circles.append(Circle((x * sym_x[i], y * sym_y[i]), R1))
            
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
            y = 1 - R1 - pend_current
            for j in range(4):
                circles.append(Circle((x * sym_x[j], y * sym_y[j]), r))
                if len(circles) == m:
                    break
                circles.append(Circle((y * sym_y[j], x * sym_x[j]), r))
                if len(circles) == m:
                    break
        return circles
                


def mathmatic_solution(m, pointList):
    circleList = []
    radius_sum = 0
    center_step = 0.01
    if m >= 1:
        circleList.append(Circle((0,0),1))
        pointList = list(filter(lambda point: valid(Circle(point, 0), circleList) ,pointList))
    for i in range(1, m):
        maxcircle = Circle((0,0),0)
        circle = 0
        for point in pointList:
            circle = Circle(point, 0)
            radius_step = 0.1
            while radius_step > 1e-5:
                if circle.radius > maxcircle.radius:
                    maxcircle = circle.copy()
                circle.radius += radius_step
                if not valid(circle, circleList):
                    circle.radius -= radius_step
                    radius_step /= 10
        if valid(maxcircle, circleList):
            circleList.append(maxcircle)
            radius_sum += maxcircle.radius**2
        pointList = list(filter(lambda point: valid(Circle(point, 0), circleList) ,pointList))

    return circleList


def main():
    rate = []
    pointStep = 0.1
    point = (-1,-1)
    
    X = np.linspace(-1, 1, 201)
    Y = np.linspace(-1, 1, 201)

    for m in range(0, 20):
        pointList = []
        for i in X:
            for j in Y:
                pointList.append((i,j))
        circles = mathmatic_solution(m, pointList)
        total = sum([cir.calAria() for cir in circles ])
        rate.append(total/4*100)
    m = np.linspace(0,19,20)
    print(m)
    print(rate)
    ax=plt.subplot(111)
    plt.sca(ax)
    plt.plot(m, rate)
    plt.show()

if __name__ == '__main__':
    main()