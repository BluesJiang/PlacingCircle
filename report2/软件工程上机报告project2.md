# <center>软件工程上机实验报告</center>
# <center>Project 2</center>
### <center>姓名：杨晨 班级：软件工程1506班 学号：U201517138</center>
### <center>结伴：蒋志远 软件工程1506班 U201517
## 问题描述
Project 2:In a box bounded by [-1, 1], given m balloons(they cannot overlap) with variable radio r and position mu. And some tiny blocks are in the box at given position {d};balloons cannot overlap with these blocks. find the optimal value of r and mu which maximizes sum r^2
## 算法描述以及改进过程
### 基本算法
对于该问题使用数值解法。
1.首先在正方形中取1000*1000的等距点阵，作为圆心的备选点。每次放一个圆之前，遍历所有备选点，在每个备选点上将圆的半径逐渐扩大，直到该圆不再满足题目中的条件时停止。记录下符合条件的半径最大的圆对应的中心坐标和半径，并存储在一个数组中。

2.判断圆是否符合条件的方法：若圆超过[-1,1]边界，则不符合条件，若圆与数组中的任何一个圆有所重叠，则不符合条件。其他情况均符合条件。

**3.project2只需在project1的基础上，加入一个向用户请求钉子的数量和位置的步骤。然后将这些钉子视为半径为0的“圆”。将这些“圆”事先放在数组中，即可以达到题目所述要求。**

### 局部优化
基本算法中，每次都需要遍历1000\*1000的点阵，浪费了很多时间。所以可以先将1000\*1000的点阵坐标存储在一个数组中，每次放一个圆，就将该圆中的点从点阵数组中删除，可以减少后面的循环次数。



## 结构和测试单元
### 定义的数据存储结构

```c
struct circle
{
    double x;
    double y;
    double radius;
};
typedef struct circle Circle;

struct circle_list
{
    Circle circle;
    struct circle_list * next;
    
};
typedef struct circle_list CircleList;
```
### 关键函数实现

```python
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
```
```python
def mathmatic_solution(m):
    circleList = []
    radius_sum = 0
    center_step = 0.01
    for i in range(0, m):
        circle = Circle((-1+center_step, -1+center_step), 0)
        maxcircle = circle.copy()
        while circle.center[0] < 1:
            circle.center = (circle.center[0]+center_step,  -1 + center_step)
            while circle.center[1] < 1:
                circle.center = (circle.center[0], circle.center[1]+center_step)
                circle.radius = 0
                radius_step = 0.1
                while radius_step > 1e-5:
                    if circle.radius > maxcircle.radius:
                        maxcircle = circle.copy()
                    circle.radius += radius_step
                    if not valid(circle, circleList):
                        circle.radius -= radius_step
                        radius_step /= 10
        if valid(maxcircle):
            circleList.append(maxcircle)
            radius_sum += maxcircle.radius**2
    return circleList
```

### 单元测试
写好了关键函数之后，对各个函数进行独立的调用，使用不同的测试用例来进行：

| Circle number | x  | y  |radius|valid()返回值|
|:-------------:|:---:|:---:|:--:|:----------:|
| 1             | -1  | -1  | 1  |0           |
| 2             |-0.88|-0.83|0.9 |0           |
| 3             |-0.83| 0.83|0.11|1           |

## 实验结果
在macOS环境下，使用tkinter绘图库，得出程序的运行结果：
<center><img src="./result2.png" width=400></center>

## 实验总结
1.根据绘图结果，发现该算法的精确度并不高，因为坐标的位置只精确到小数点后两位，半径只精确到小数点后5位。所以该算法只是对原问题运用了数值解法得到的一个近似解。

##附录
### Git log
<center><img src="./gitlog1.png" width=500></center>