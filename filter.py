from depedent_packages import *


# 设计低通滤波器
def lowpass_filter(signal, cutoff_freq, sampling_rate):
    # 计算傅里叶变换
    freq_domain_signal = np.fft.fft(signal)
    # 计算频率轴
    freqs = np.fft.fftfreq(len(signal), 1/sampling_rate)
    # 设计低通滤波器
    filter_mask = np.abs(freqs) <= cutoff_freq
    # 应用滤波器
    filtered_signal_freq = freq_domain_signal * filter_mask
    # 逆傅里叶变换回到时域
    filtered_signal = np.fft.ifft(filtered_signal_freq)
    return np.real(filtered_signal)

# 设计高通滤波器
def highpass_filter(signal, cutoff_freq, sampling_rate):
    # 计算傅里叶变换
    freq_domain_signal = np.fft.fft(signal)
    # 计算频率轴
    freqs = np.fft.fftfreq(len(signal), 1/sampling_rate)
    # 设计高通滤波器
    filter_mask = np.abs(freqs) > cutoff_freq
    # 应用滤波器
    filtered_signal_freq = freq_domain_signal * filter_mask
    # 逆傅里叶变换回到时域
    filtered_signal = np.fft.ifft(filtered_signal_freq)
    return np.real(filtered_signal)
