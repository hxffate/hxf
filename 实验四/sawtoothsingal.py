import os
import matplotlib.pyplot as plt
import playsound
from th import CosSignal, SinSignal
cos_sig = CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = SinSignal(freq=880, amp=0.5, offset=0)
from th import decorate
from th import SquareSignal
from th import TriangleSignal
def filter_spectrum(spectrum):
    """Divides the spectrum through by the fs.

    spectrum: Spectrum object
    """
    # avoid division by 0
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0

signal = TriangleSignal(440)

duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
sqr=segment.make_spectrum()

#segment.plot()
decorate(xlabel='Time (s)')
wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()
spectrum = wave.make_spectrum()
filter_spectrum(sqr)
sqr.plot()
plt.show()
print(spectrum.fs[0]);
print(spectrum.fs[1]);
print(spectrum.fs[2]);
print(spectrum.fs[3]);
spectrum.hs[0]=100
print(spectrum.hs[0]);
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
wave.write('sawtooth2.wav')
#plt.show()
from th import TriangleSignal
from th import decorate

signal = TriangleSignal(440)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
wave1 = signal.make_wave(duration=0.5, framerate=10000)
wave1.apodize()
wave1.make_audio()
wave1.write('sawtooth.wav')
# segment.plot()
# decorate(xlabel='Time (s)')
# plt.show()
from th import Sinusoid
from th import normalize, unbias
import numpy as np


# class SawtoothSignal(Sinusoid):
#     """Represents a sawtooth signal."""
#
#     def evaluate(self, ts):
#         """Evaluates the signal at the given times.
#
#         ts: float array of times
#
#         returns: float wave array
#         """
#         cycles = self.freq * ts + self.offset / np.pi / 2
#         frac, _ = np.modf(cycles)
#         ys = normalize(unbias(frac), self.amp)
#         return ys
#
#
#     sawtooth.plot()
#     plt.show()

