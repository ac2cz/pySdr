# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:59:28 2018

@author: g0kla@arrl.net
"""
import matplotlib.pyplot as plt
import dsp
import numpy as np
import math

def main():
    sig = []
    sample_len = 128
    osc = dsp.Oscillator(1200, 48000)
    for n in range(0, sample_len):
        sig.append(osc.next_sample())
    #plt.plot(sig, label='1200Hz')
    out = np.fft.rfft(sig)
    psd = []
    psd.append(out[0].real)
    half = int(len(out))
    for k in range(1, half):
        psd.append(math.sqrt(out[k].real*out[k].real + out[k].imag*out[k].imag))
    psd[half-1] = math.sqrt(out[0].imag*out[0].imag + out[half-1].imag*out[half-1].imag)
    plt.plot(psd, label='FFT')
    plt.show()
main()
