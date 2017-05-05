


import math

class Circle():
    center = (0, 0) 
    radius = 0
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def description(self):
        return ("Center: (%.2e, %.2e)\tRadius:%.2e"%(self.center[0], self.center[1], self.radius))


def sub_solution_r(m):
    circles = []
    circles.append(Circle((0, 0), 1))
    sym_x = [1, 1, -1, -1]
    sym_y = [1, -1, 1, -1]
    if m == 1:
        return circles
    elif m <= 5:
        r = 3 - 2 * math.sqrt(2)
        y = x = 1 - r
        for i in range(0, 4):
            circles.append(Circle((x * sym_x[i], y * sym_y[i]), r))
        return circles
    elif m > 5:
        r0 = 3 - 2 * math.sqrt(2)
        radius = [r0]
        y = x = 1 - r0
        for i in range(0, 4):
            circles.append(Circle((x * sym_x[i], y * sym_y[i]), r0))
        pend_height = 0
        k = m - 5
        if k % 8 == 0:
            k = int(k / 8)
        else:
            k = int(k / 8) + 1
        pend_current = 0
        for i in range(1, k+1): 
            r = ((1 - pend_current - r0)/ (2 * (1+math.sqrt(radius[i-1])))) ** 2
            pend_current += 2 * math.sqrt(r * radius[i-1])
            radius.append(r)
            x = 1 - r
            y = 1 - r0 - pend_current
            for j in range(4):
                circles.append(Circle((x * sym_x[j], y * sym_y[j]), radius[i]))
                if 8*(i-1)+j+5+1>8:
                    break
                circles.append(Circle((y * sym_y[j], x * sym_x[j]), radius[i]))
                if 8*(i-1)+j+5>8:
                    break
        return circles
                




def main():
    for circle in sub_solution_r(15):
        print(circle.description())

if __name__ == '__main__':
    main()