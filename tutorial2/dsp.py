# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:59:28 2018
@author: g0kla@arrl.net
"""
import math

class Oscillator:
    """A Numerically Controlled Oscillator
    """
    TABLE_SIZE = 128

    def __init__(self, frequency, samples):
        self.freq = frequency
        self.sampleRate = samples
        self._phase = 0
        self._sinTable = self._init_table()
        self._phaseIncrement = self._calc_phase_inc(self.freq, self.sampleRate)
        
    def _init_table(self):
        table = []
        for n in range(0, self.TABLE_SIZE):
            table.append(math.sin(n*2.0*math.pi/self.TABLE_SIZE))
        return table
    
    def _calc_phase_inc(self, frequency, samplesPerSecond):
        return 2 * math.pi * frequency / samplesPerSecond

    def next_sample(self):
        self._phase = self._phase + self._phaseIncrement
        if (self._phase >= 2 * math.pi):
            self._phase = 0;
        idx = (int)((self._phase * self.TABLE_SIZE/(2 * math.pi))%self.TABLE_SIZE)
        value = self._sinTable[idx]
        return value

    
