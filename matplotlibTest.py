# coding=utf-8
"""
created on:2018/4/23
author:DilicelSten
target:learn matplotlib
"""
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------line-----------------------------
#
x = np.linspace(-np.pi, np.pi, 256,endpoint=True)
c, s = np.cos(x), np.sin(x)  # 定义余弦和正弦函数
plt.figure(1)
plt.plot(x, s, color="blue", linewidth=1.0, linestyle="-", label="COS", alpha=0.5)  # 绘图及属性
plt.plot(x, c, "r*", label="SIN")
plt.title("COS & SIN")  # 加标题
ax = plt.gca()  # 轴的编辑器
# 出现横轴和纵轴
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))
ax.yaxis.set_ticks_position("left")
ax.xaxis.set_ticks_position("bottom")
# 扩大横纵轴上的数标
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.2))
# 出现图例
plt.legend(loc="upper left")
# 出现网格线
plt.grid()
# 限制范围
# plt.axis([-1, 1, -0.5, 1])
# 填充功能
plt.fill_between(x, np.abs(x) < 0.5, c, c > 0.5, color="green", alpha=0.5)
# 注释功能
t = 1
plt.plot([t, t], [0, np.cos(t)], 'y', linewidth=3, linestyle="--")
plt.annotate("cos(1)", xy=(t, np.cos(1)), xycoords="data", xytext=(+10, +30), textcoords="offset points", arrowprops=dict(connectionstyle="arc3,rad=0.2"))
plt.show()

# ----------------------many type of figures--------------------------
# 散点图
fig = plt.figure()  # 建立表格
fig.add_subplot(3, 3, 1)  # 3行3列
n = 128
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)  # 上色
# plt.axes([0.025, 0.025, 0.95, 0.95])  # 确定显示范围
plt.scatter(X, Y, s=75, c=T, alpha=0.5)  # 画散点
plt.xlim(-1.5, 1.5)
plt.xticks([])
plt.ylim(-1.5, 1.5)
plt.yticks([])
plt.axis()
plt.title("scatter")
plt.xlabel("x")
plt.ylabel("y")


# 柱状图
fig.add_subplot(3, 3, 2)
n = 10
X = np.arange(n)
Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
plt.bar(X, +Y1, facecolor="#9999ff", edgecolor="white")
plt.bar(X, -Y2, facecolor="#ff9999", edgecolor="white")
# 添加注释
for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha="center", va="bottom")
for x, y in zip(X, Y2):
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha="center", va="top")


# 饼图
fig.add_subplot(333)
n = 20
Z = np.ones(n)
Z[-1] *= 2
plt.pie(Z, explode=Z * .05, colors=['%f' % (i / float(n)) for i in range(n)], labels=['%2f' % (i / float(n)) for i in range(n)])
plt.gca().set_aspect('equal')  # 正圆
plt.xticks([])
plt.yticks([])


# 极坐标
fig.add_subplot(334, polar=True)
n = 20
theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / n)
radii = 10 * np.random.rand(n)  # 半径
# plt.plot(theta, radii)
plt.polar(theta, radii)

# 热图
fig.add_subplot(335)
from matplotlib import cm  # 上色
data = np.random.rand(3, 3)
cmap = cm.Blues
map = plt.imshow(data, interpolation='nearest', cmap=cmap, aspect='auto', vmin=0, vmax=1)


# 3D图
from mpl_toolkits.mplot3d import Axes3D
ax = fig.add_subplot(336, projection="3d")
ax.scatter(1, 1, 3, s=100)


# 热力图
fig.add_subplot(313)
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
plt.savefig('fig.png')
plt.show()