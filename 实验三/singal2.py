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
wave = read_wave('170255__dublie__trumpet.wav')
wave.normalize()
wave.make_audio()
#plt.subplot(1,1,1)
#wave.plot()
#plt.show()
segment = wave.segment()
segment.make_audio()
spectrum = segment.make_spectrum()
spectrum.high_pass(1000)
spectrum.make_wave().make_audio()
wave2=spectrum.make_wave()
wave2.write('high.wav')
spectrum.low_pass(5000)
wave3=spectrum.make_wave()
wave3.write('low.wav')
spectrum2 = segment.make_spectrum()
spectrum2.band_stop(1000,5000)
wave4=spectrum2.make_wave()
wave4.write('band.wav')
single=(SinSignal(freq=40,amp=1000)+CosSignal(freq=60,amp=1500))

#plt.subplot(1,1,1)
#single.plot()



wave5=single.make_wave()
wave5.normalize()
wave5.make_audio()
wave5.write('sin+cos.wav')
#plt.show()

wave.normalize()
wave.make_audio()
def stretch(wave,factor):
    wave.ts*=factor
    wave.framerate/=factor
stretch(wave, 0.5)
wave6=spectrum.make_wave()
wave6.write('strecth.wav')
wave3.make_audio()
plt.subplot(1,1,1)
wave3.plot()
plt.show()
