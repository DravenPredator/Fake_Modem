import matplotlib.pylab as plt
import numpy as np
'''
    Author: Rowland DePree          FSK.py

    A class to modulate and de-modulate a binary string using FSK
'''

class FSK:
    def __init__(self, message):
        self.signal = message
        self.wave_math = []

    def encode_wave(self):

        plt.figure('FSK')

        x = np.linspace(0, 2 * np.pi, 201)
        if self.signal[0] == 1:
            plt.plot(x, (np.sin(2 * x)), 'b')
            self.wave_math.append('sin(2x)')
        else:
            plt.plot(x, np.sin(x), 'b')
            self.wave_math.append('sin(x)')

        for num in range(1, len(self.signal)):
            y = np.linspace((num * 2) * np.pi, (num * 2 + 2) * np.pi, 201)
            if self.signal[0] == 0:
                if self.signal[num] == 0:
                    plt.plot(y, np.sin(y), 'b')
                    self.wave_math.append('sin(x)')
                else:
                    plt.plot(y, np.sin(2 * y), 'b')
                    self.wave_math.append('sin(2x)')
            else:
                if self.signal[num] == 1:
                    plt.plot(y, np.sin(y * 2), 'b')
                    self.wave_math.append('sin(2x)')
                else:
                    plt.plot(y, np.sin(y), 'b')
                    self.wave_math.append('sin(x)')

    def decode_wave(self):
        digital_message = []
        for element in self.wave_math:
            if element == 'sin(x)':
                digital_message.append(0)
            if element == 'sin(2x)':
                digital_message.append(1)

        return digital_message
