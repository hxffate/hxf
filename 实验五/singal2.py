# Get th.py
import os
import matplotlib.pyplot as plt
import playsound
from th import CosSignal, SinSignal
cos_sig = CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = SinSignal(freq=880, amp=0.5, offset=0)
from th import decorate
import os
from th import read_wave
from IPython.display import Audio
import numpy as np
from th import SinSignal
# signal = SinSignal(freq=440)
# duration = signal.period * 30.25
# wave = signal.make_wave(duration)
# spectrum = wave.make_spectrum()
# spectrum.plot(high=880)
# decorate(xlabel='Frequency (Hz)')
# #plt.show()



from th import Chirp
from th import normalize, unbias

PI2 = 2 * np.pi

class SawtoothChirp(Chirp):
    """Represents a sawtooth signal with varying frequency."""

    def evaluate(self, ts):
        """Helper function that evaluates the signal.

        ts: float array of times
        """
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys

signal = SawtoothChirp(start=0, end=100)
wave3 = signal.make_wave(duration=1, framerate=2000)
wave3.apodize()
wave3.make_audio()
spectrum2 = wave3.make_spectrum()
wave3.plot()
wave3.write('temp.wav')
plt.show()

# from th import read_wave
# read_wave('tos-redalert.wav').make_audio()
# wave.write('temp2.wav')

# from th import Chirp
# signal = Chirp(start=2500, end=3000)
# wave1 = signal.make_wave(duration=2)
# wave1.make_audio()
# wave.write('temp3.wav')
class TromboneGliss(Chirp):
    """Represents a trombone-like signal with varying frequency."""

    def evaluate(self, ts):
        """Evaluates the signal at the given times.

        ts: float array of times

        returns: float wave array
        """
        l1, l2 = 1.0 / self.start, 1.0 / self.end
        lengths = np.linspace(l1, l2, len(ts))
        freqs = 1 / lengths

        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        ys = self.amp * np.cos(phases)
        return ys

low = 262
high = 349
signal = TromboneGliss(high, low)
wave1 = signal.make_wave(duration=1)
wave1.apodize()
wave1.make_audio()


signal = TromboneGliss(low, high)
wave2 = signal.make_wave(duration=1)
wave2.apodize()
wave2.make_audio()
wave = wave1 | wave2
wave.make_audio()
spectrum = wave.make_spectrum()
spectrum.plot()
wave.write('temp2.wav')
plt.show()
