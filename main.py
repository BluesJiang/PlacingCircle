


import math
import numpy as np
from matplotlib import pyplot as plt

circleList = []
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


def valid(circle):
    
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
                





def main():
    rate = []
    for m in range(0, 100):
        circles = sub_solution_r(m)
        
        total = sum([cir.calAria() for cir in circles ])
        rate.append(total/4*100)
    m = np.linspace(0,99,100)
    print(m)
    print(rate)
    ax=plt.subplot(111)
    plt.sca(ax)
    plt.plot(m, rate)
    plt.show()

if __name__ == '__main__':
    main()