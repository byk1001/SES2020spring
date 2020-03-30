import unittest
import matplotlib.pyplot as plt
import numpy as np

from plot import search, plotCircle, circle
class TestClass1(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(True, True)

class Test_circle:
    #圆心坐标(x,y)
    #半径 r
    x = 0
    y = 0
    r = 0

    # 定义构造函数。输入变量为圆心坐标及半径
    def __init__(self, x, y, r):
        # self.center = complex(x, y)
        self.x = x
        self.y = y
        self.r = abs(r)

    def get_Distance(self,c):
        D=abs(self.x-c.x)+abs(self.y-c.y)
        return D

def test_check(self,circleList):  ##检查圆与圆是否重叠或超出边界
    if self.x + self.r > 1 or self.x - self.r < -1 or self.y + self.r > 1 or self.y-self.r < -1:  ##圆超出边界，返回false(0)
        return 0
    for c in circleList:
        if self.getDistance(self,c)<(self.r+c.r):
            return 0
    return 1
def test_search(circleList):  ##在circleList的基础上，找新的符合条件的最大圆
    max_r = 0    ##max_r用于存储最大的半径的圆，初始化为0
    max_x = 0
    max_y = 0
    state=1
    for x in range(-100,100,1):  ##range的分度值似乎不能输入0.01，因此扩大一百倍凑成整数
        x = x / 100
        for y in range(-100,100,1):
            y = y / 100
            for c in circleList:
                if (x-c.x)**2+(y-c.y)**2<c.r**2:
                    state=0
            if state==0:
                state=1
                continue
            r=min(abs(x+1),abs(1-x),abs(y+1),abs(y-1))  ##新圆的半径初始化为到边界最短距离
            for c in circleList:    ##再看r会不会太大，与其他圆相交
                if (x-c.x)**2+(y-c.y)**2<(c.r+r)**2:
                    r=((x-c.x)**2+(y-c.y)**2)**0.5-c.r ##若相交，改变r为相切时的半径
            if r>max_r:  ##存储最大的半径的圆，之后会输入circleList
                max_r=r
                max_x=x
                max_y=y
    new=circle(max_x,max_y,max_r)
    ##print(max_x,max_y,max_r)  ##输出圆的坐标，半径
    circleList.append(new)

def test_plotCircle(circleList):  ##对给定的圆心(x,y)和半径r画圆
    plt.figure()
    plt.axes().set_aspect('equal')
    plt.xlim([-1, 1])    ##限制作图的坐标系在-1到1之间
    plt.ylim([-1, 1])
    theta = np.linspace(0, 2 * np.pi, 90)
    for c in circleList:
        plt.plot(c.x + c.r * np.cos(theta), c.y + c.r * np.sin(theta), 'b')
    plt.show()

n=7   ################在此输入圆的个数n  ######################
if n>0:
    cList=[]
    while(n):  ##利用贪心算法，第n次search()是基于第n-1次search()得到的最优解，即从n=1时开始找
        search(cList)
        n-=1
    plotCircle(cList)



if __name__ == '__main__':
    unittest.main()
