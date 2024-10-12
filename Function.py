from depedent_packages import *
from filter import *
class Function:
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

    def filter_wavelet(signal, wavelet='db4', level=1, type='lowpass'):
        """
        对给定的数据进行小波变换，并返回指定层次的近似系数和细节系数。

        参数:
        data -- 待处理的数据
        wavelet -- 小波基
        level -- 小波变换的层次

        返回值:
        (cA, cD) -- 近似系数和细节系数
        """
        assert type in ['lowpass', 'highpass'], 'type must be "lowpass" or "highpass"'
        assert level > 0, 'level must be greater than 0'
        if type == 'lowpass':
            coeffs = pywt.wavedec(signal, wavelet, mode='symmetric', level=1)
            # coeffs[0] 是低频分量 (approximation coefficients)
            return pywt.waverec([coeffs[0]] + [np.zeros_like(c) for c in coeffs[1:]], wavelet)
        else:
            coeffs = pywt.wavedec(signal, wavelet, mode='symmetric', level=1)
            # coeffs[1] 是高频分量 (detail coefficients)
            return pywt.waverec([np.zeros_like(c) for c in coeffs[:-1]] + [coeffs[-1]], wavelet)

    def filter_fft(signal, cutoff_freq=30 , sampling_rate=1000,  type='lowpass'):
        """
        对给定的数据进行傅里叶变换，并返回指定截止频率的低通或高通滤波结果。整个序列为一个时钟，简而言之，如果该序列包含50个周期，那么它的频率就是50Hz。
        采样频率是指在一秒钟内对信号进行采样的次数。例如，如果采样频率为1000Hz，那么在一秒钟内对信号进行1000次采样。

        参数:
        data -- 待处理的数据
        cutoff -- 截止频率
        type -- 滤波类型

        返回值:
        result -- 滤波结果
        """
        assert type in ['lowpass', 'highpass'], 'type must be "lowpass" or "highpass"'
        if cutoff_freq > sampling_rate/2:
            raise Warning('cutoff frequency must be less than Nyquist frequency')
        fft = np.fft.fft(signal)
        if type == 'lowpass':
            result = lowpass_filter(signal, cutoff_freq, sampling_rate)
        else:
            result = highpass_filter(signal, cutoff_freq, sampling_rate)
        return result
    
    
