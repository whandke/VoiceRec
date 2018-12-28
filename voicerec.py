import sys
import numpy as np
import numpy.fft as fft
import scipy.io.wavfile as wavfile
from scipy.signal import hamming
import matplotlib
import matplotlib.pyplot as plt
plt.style.use(['dark_background', 'ggplot'])

if __name__ == '__main__':

    voice = sys.argv[1]

    rate, data = wavfile.read(voice)
    data = data.astype(float) / 2**16
    if not isinstance(data[0], float):
        data = data[:, 0] + data[:, 1]
    rate = float(rate)
    time = len(data) / rate

    processed = data * hamming(len(data))

    plt.plot(np.arange(0, time, 1/rate), processed, linewidth=1.0)
    plt.show()
