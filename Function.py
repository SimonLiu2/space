import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
def draw_circle_with_half_filled(ax, direction='right',center=(0,0), radius=1, edgecolor='black', facecolor='none', fillcolor='black'):
    """
    在给定的ax上绘制一个圆，并填充右半圆为指定颜色。

    参数:
    ax -- 绘图对象
    center -- 圆心坐标 (x, y)
    radius -- 圆的半径
    edgecolor -- 圆的边框颜色
    facecolor -- 圆的填充颜色
    fillcolor -- 右半圆的填充颜色
    """
    assert direction in ['right', 'left'], 'direction must be "right" or "left"'
    assert type(ax) == plt.Axes, 'ax must be a matplotlib.axes.Axes instance'

    # 添加圆
    circle = patches.Circle(center, radius, edgecolor=edgecolor, facecolor=facecolor)
    ax.add_patch(circle)

    # 填充右半圆为指定颜色
    if direction == 'right':
        half_circle = patches.Wedge(center, radius, 270, 90, facecolor=fillcolor)
    else:
        half_circle = patches.Wedge(center, radius, 90, 270, facecolor=fillcolor)
    ax.add_patch(half_circle)

def draw_3Dsphere(ax, color='b', radius=1, alpha=0.5):
    """
    在给定的ax上绘制一个3D球体。
    参数:
    ax -- 绘图对象
    color -- 球体的颜色
    radius -- 球体的半径
    alpha -- 球体的透明度
    """
    assert type(ax) == plt.Axes, 'ax must be a matplotlib.axes.Axes instance'

    # 添加球体
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radius*np.outer(np.cos(u), np.sin(v))
    y = radius*np.outer(np.sin(u), np.sin(v))
    z = radius*np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color=color, alpha=alpha)
def test():
    pass