"""
Sound Card Test
"""
from pysoundcard import Stream
import numpy as np
import math
import sdrgui
import threading

reading_data = True
win = sdrgui.MainWindow()

def average (avg, new_sample, N):
    avg = avg - avg / N
    avg = avg + new_sample / N
    return avg

def calc_psd(re, im, bin_bandwidth):
    power = math.sqrt((re*re) + (im*im))/bin_bandwidth
    if (power == 0):
        power = 1E-20
    val = 20 * math.log10( power )
    return val
	
def audio_thread():
    print("Starting Audio")
    global reading_data
    global win
    fs = 48000
    fftLength = 255
    blocksize = 255
    bin_bandwidth = fs/fftLength
    avg_num = 10
    
    s = Stream(samplerate=fs, blocksize=blocksize)
    s.start()
    psd = [0] * fftLength
    while reading_data:
        data = s.read(fftLength)
        left, right = map(list, zip(*data))
        out = np.fft.rfft(left)
        
        psd[0] = average(psd[0], calc_psd(out[0].real,out[0].real,bin_bandwidth), avg_num)
        half = int(len(out))
        for k in range(1, half):
            psd[k] = average(psd[k], calc_psd(out[k].real,out[k].imag,bin_bandwidth), avg_num)
        psd[half-1] = average(psd[k], calc_psd(out[0].imag, out[half-1].imag,bin_bandwidth), avg_num)
        if (reading_data):
            win.setData(psd)
    s.stop()

def main():
    print("SDR Audio Test")
    threading.Thread(target=audio_thread).start() 
    win.start()
    reading_data = False
       
main()
