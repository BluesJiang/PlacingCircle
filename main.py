


import math

class Circle():
    center = (0, 0) 
    radius = 0
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def description(self):
        return ("Center: (%f, %f)\tRadius:%.10f"%(self.center[0], self.center[1], self.radius))


def sub_solution_r(m):
    circles = []
    R = [1]
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
    for circle in sub_solution_r(26):
        print(circle.description())

if __name__ == '__main__':
    main()