import sys
import numpy as np
from numpy.fft import fft
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import matplotlib
import matplotlib.pyplot as plt
plt.style.use(['dark_background', 'ggplot'])

subs = 6


def hps(data, rate, iter):
    processed = data * signal.hamming(len(data))
    processed = np.fft.rfft(processed)
    processed = abs(processed)

    ds2 = signal.decimate(processed, 2)
    ds3 = signal.decimate(processed, 3)
    ds4 = signal.decimate(processed, 4)
    ds5 = signal.decimate(processed, 5)

    l = len(ds5)

    new = processed[:l] * ds2[:l] * ds3[:l] * ds4[:l] * ds5[:l]

    plt.subplot(subs, 1, 1)
    plt.plot(processed[:l])

    plt.subplot(subs, 1, 2)
    plt.plot(ds2[:l])

    plt.subplot(subs, 1, 3)
    plt.plot(ds3[:l])

    plt.subplot(subs, 1, 4)
    plt.plot(ds4[:l])

    plt.subplot(subs, 1, 5)
    plt.plot(ds5[:l])

    plt.subplot(subs, 1, 6)
    plt.plot(new[:l])

    lcf = 50

    result = np.argmax(new[lcf:]) + lcf
    div = len(data) / rate

    return result / div

if __name__ == '__main__':

    voice = sys.argv[1]

    rate, data = wavfile.read(voice)
    data = data.astype(float) / 2**16
    if not isinstance(data[0], float):
        data = data[:, 0] + data[:, 1]
    rate = float(rate)

    time = len(data) / rate

    result = hps(data, rate, 4)

    ans = 'M'
    if result > 170:
        ans = 'K'

    print(ans)

    plt.show()
