# <center>软件工程上机实验报告</center>
# <center>Project 2</center>

|姓名|学号|班级|
|:---:|:----:|:---:|
|蒋志远|U201517149|软工1506|
|杨晨|U201517138|软工1506|
|李露阳|U201517132|软工1506|

## 问题描述
Project 3:In a box(3D) bounded by $[-1, 1]$, given m balloons(they cannot overlap) with variable radio $r$ and position $mu$. And some tiny blocks are in the box at given position ${d}$;balloons cannot overlap with these blocks. find the optimal value of $r$ and $mu$ which maximizes $\sum r^3$
## 算法描述以及改进过程
### 基本算法
对于该问题使用数值解法。

1. 首先在正方体中中取$200\times200\times200$的等距点阵，作为球心的备选点。每次放一个球之前之前，遍历所有备选点，在每个备选点求出可以满足条件的最大半径。记录下符合条件的半径最大的圆对应的中心坐标和半径，并存储在一个数组中。

2. 求球的最大半径的方法：记球心的坐标为$(x,y,z)$,半径为$r$,则在$|x-1|$, $|x+1|$, $|y+1|$, $|y-1|$, $|z+1|$, $|z-1|$和与各个已存在的球相切的半径中选出一个最小的值，即为当前满足条件的最大的球的半径。



### 局部优化
基本算法中，每次都需要遍历$200\times200\times200$的点阵，浪费了很多时间。所以可以先将$200\times200\times200$的点阵坐标存储在一个数组中，每次放一个球，就将该球中的点从点阵数组中删除，可以减少后面的循环次数。



## 结构和测试单元
### 关键函数实现

```java
//找出(x,y,z)点处的最大半径
public double MaxValidRadius(double x, double y, double z) {
        ArrayList<Double> radiusList = new ArrayList<>();
        radiusList.add(Math.abs(x + 1));
        radiusList.add(Math.abs(x - 1));
        radiusList.add(Math.abs(y + 1));
        radiusList.add(Math.abs(y - 1));
        radiusList.add(Math.abs(z + 1));
        radiusList.add(Math.abs(z - 1));

        Point p = new Point(x, y, z);

        Circle tmp = new Circle(p, 0);

        for (Circle circle : circleList) {
            radiusList.add(distance(tmp, circle) - circle.radius);
        }


        for (Point pin : pinList) {
            Circle _pin = new Circle(pin, 0);
            radiusList.add(distance(tmp, _pin));
        }


        double max_radius = radiusList.get(0);
        for (double radius : radiusList) {
            if (radius < max_radius) {
                max_radius = radius;
            }
        }

        return max_radius;


    }
```

### 单元测试
写好了关键函数之后，对各个函数进行独立的调用，使用不同的测试用例来进行：

| Circle number | x   | y   | z   |maxValidRadius()返回值|
|:-------------:|:---:|:---:|:---:|:----------:|
| 1             | -0.4| -0.5| 0.3 |0.5         |
| 2             |-0.68|0.43 |-0.65|0.32        |
| 3             |-0.13|-0.4 |0.8  |0.2         |

## 实验结果
在macOS环境下，使用javafx绘图库，得出程序的运行结果：
<center><img src="img/result4.png" width=275>

## 实验总结
1. 根据绘图结果，发现该算法的精确度并不高，因为坐标的位置只精确到小数点后两位,所以该算法只是对原问题运用了数值解法得到的一个近似解。
2. 图中可以看出有一些圆并没有相切，因为计算机精度的原因，计算时会出现舍入误差，因为画图是映射到像素，所以每个点的间距被扩大了200倍，所以造成有缘没有相切

##附录
### Git log
```
commit b9805791d602bdaf1e6b54436d743dcbc550d32c
Author: ChAnYaNG97 <790194334@qq.com>
Date:   Thu Jun 1 17:13:48 2017 +0800

    add pictures

commit 801f2f067a25410b7a58da98030f4194b52e1aad
Author: ChAnYaNG97 <790194334@qq.com>
Date:   Thu Jun 1 16:52:25 2017 +0800

    add reports

commit f26b0d0043b1107abbb3e29d9603c3b9fea91dd4
Author: ChAnYaNG97 <790194334@qq.com>
Date:   Thu Jun 1 16:50:00 2017 +0800

    add reports

commit 90145474f66d066a154b68a80184bffec33d41ad
Author: BluesJiang <763400095@qq.com>
Date:   Thu Jun 1 16:48:23 2017 +0800

    add block

commit 78037db21cbf1a8ed5dabcaec93c87f6a3752614
Merge: 2d98dec 21d5a13
Author: BluesJiang <763400095@qq.com>
Date:   Thu Jun 1 16:33:27 2017 +0800

    comma conflict

commit 2d98decdae4bc292c4aaffa8bb24019e316b8b15
Author: BluesJiang <763400095@qq.com>
Date:   Thu Jun 1 16:32:32 2017 +0800

    comma

commit 21d5a13c0d7fb17317a2337da2d3fdb67e6e6463
Author: ChAnYaNG97 <790194334@qq.com>
Date:   Thu Jun 1 16:25:05 2017 +0800

    delete comma

commit 41ff89e80dfab167f85a3a7ec72a46bd3309ff12
Merge: 85e80bc 74e49b3
Author: ChAnYaNG97 <790194334@qq.com>
Date:   Thu Jun 1 16:23:30 2017 +0800

    conflict fixed

commit 85e80bca92d8bab2363aac92420c59142932fd66
Author: ChAnYaNG97 <790194334@qq.com>
Date:   Thu Jun 1 16:14:30 2017 +0800

    draw

commit 74e49b3589957c380187adc3ae5191ebcd379fdc
Author: BluesJiang <763400095@qq.com>
Date:   Thu Jun 1 16:13:57 2017 +0800

    accelerate

commit 403f67663bf1b80ca336f2bb9eaaaa2572496551
Author: BluesJiang <763400095@qq.com>
Date:   Thu Jun 1 15:09:37 2017 +0800

    fix some bug

commit ec93a62e3e7d904221826f8d849e3345a021f6b0
Merge: f5eb45d d82cba8
Author: BluesJiang <763400095@qq.com>
Date:   Thu Jun 1 14:54:23 2017 +0800

    fix comflict

commit f5eb45d86bc23f997e728682be3082a995c97438
Author: BluesJiang <763400095@qq.com>
Date:   Thu Jun 1 14:50:13 2017 +0800

    translate addCicle

commit d82cba85e78f028f3c50c9e724a9a92691d0ee8a
Author: ChAnYaNG97 <790194334@qq.com>
Date:   Thu Jun 1 14:46:25 2017 +0800

    some corrections

commit cda36f61a8aa18d7f4e4ff72883012b05a6617dc
Author: ChAnYaNG97 <790194334@qq.com>
Date:   Thu Jun 1 14:44:58 2017 +0800

    implement the valid() function

commit 65f387a5482643e791efe8374bc684574f2f2681
Author: BluesJiang <763400095@qq.com>
Date:   Thu Jun 1 14:32:17 2017 +0800

    add distance

commit 9e9c441469f16ee13c8797c1fb0817bc846a0eb2
Author: BluesJiang <763400095@qq.com>
Date:   Thu Jun 1 11:43:50 2017 +0800

    fix when m < 3 ,result goes wrong

commit 834494816cb0729923c505ecef89a2ee0131e7bd
Author: BluesJiang <763400095@qq.com>
Date:   Thu Jun 1 10:56:47 2017 +0800

    bug fixed

commit 017a074fc3b1b28dc07fd1314ae2fb13aa485ecd
Author: BluesJiang <763400095@qq.com>
Date:   Thu Jun 1 10:30:55 2017 +0800

    clear the formula

commit c851ac95780a02f307bbac35886900cb99cc4af2
Author: BluesJiang <763400095@qq.com>
Date:   Fri May 5 20:45:27 2017 +0800

    sub_solution

```