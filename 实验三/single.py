# Get th.py
import os
import matplotlib.pyplot as plt
import playsound
from th import CosSignal, SinSignal
cos_sig = CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = SinSignal(freq=880, amp=0.5, offset=0)
from th import decorate
mix = sin_sig + cos_sig
mix
# plt.subplot(1,4,1)
cos_sig.plot()
decorate(xlabel='Time (s1)')
# plt.subplot(1,4,2)
sin_sig.plot()
decorate(xlabel='Time (s2)')
# plt.show()
wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
# plt.subplot(1,4,3)
mix.plot()
decorate(xlabel='Time (s3)')
wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
wave
from IPython.display import Audio
audio = Audio(data=wave.ys, rate=wave.framerate)
audio
wave.make_audio()
print('Number of samples', len(wave.ys))
print('Timestep in ms', 1 / wave.framerate * 1000)
period = mix.period
segment = wave.segment(start=0, duration=period*3)
# plt.subplot(1,4,4)
segment.plot()
decorate(xlabel='Time (s)')

wave.normalize()
wave.apodize()
#plt.subplot(1,2,1)
wave.plot()
decorate(xlabel='Time (s)')

# start = 1.2
# duration = 0.6
# segment = wave.segment(start, duration)
# plt.subplot(1,4,2)
# segment.plot()
# decorate(xlabel='Time (s)')
#
#
# spectrum = segment.make_spectrum()
#
# plt.subplot(1,4,3)
# spectrum.plot()
# decorate(xlabel='Frequency (Hz)')

wave.write('temp.wav')
from th import play_wave
play_wave(filename='temp.wav', player='aplay')
from th import read_wave
wave = read_wave('92002__jcveliz__violin-origional.wav')
wave.make_audio()
start = 1.2
duration = 0.6
segment = wave.segment(start, duration)
#plt.subplot(1,2,2)
segment.plot()
decorate(xlabel='Time (s)')

spectrum = segment.make_spectrum()
#plt.subplot(1,2,1)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
#plt.subplot(1,2,2)
spectrum.plot(high=10000)
decorate(xlabel='Frequency (Hz)')
#plt.subplot(1,2,1)
spectrum.low_pass(3000)
spectrum.plot(high=10000)
decorate(xlabel='Frequency (Hz)')
filtered = spectrum.make_wave()
filtered.normalize()
filtered.apodize()
#plt.subplot(1,2,2)
filtered.plot()
decorate(xlabel='Time (s)')
segment.normalize()
segment.apodize()
#plt.subplot(1,2,1)
segment.plot()
decorate(xlabel='Time (s)')

segment.make_audio()
filtered.make_audio()

import matplotlib.pyplot as plt
from IPython.display import display


def filter_wave(wave, start, duration, cutoff):
    """Selects a segment from the wave and filters it.

    Plots the spectrum and displays an Audio widget.

    wave: Wave object
    start: time in s
    duration: time in s
    cutoff: frequency in Hz
    """
    segment = wave.segment(start, duration)
    spectrum = segment.make_spectrum()
    spectrum.plot(color='0.7')
    spectrum.low_pass(cutoff)
    spectrum.plot(color='#045a8d')
    decorate(xlabel='Frequency (Hz)')
    plt.show()

    audio = spectrum.make_wave().make_audio()
    display(audio)
from ipywidgets import interact, fixed

wave = read_wave('92002__jcveliz__violin-origional.wav')
interact(filter_wave, wave=fixed(wave),
    start=(0, 5, 0.1), duration=(0, 5, 0.1), cutoff=(0, 10000, 100));


from IPython.display import Audio
audio = Audio(data=wave.ys, rate=wave.framerate)

wave.make_audio()
wave.write('temp.wav')
from th import play_wave
play_wave(filename='temp.wav', player='aplay')
from th import read_wave
wave = read_wave('92002__jcveliz__violin-origional.wav')
wave.make_audio()