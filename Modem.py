import matplotlib.pyplot as plt
import numpy as np
from FSK import FSK

'''
    Author: Rowland DePree          Modem.py

    This program demostrates the working mechanism of a modem.  It will take a binary string and covert that to
    an analogue representation.  Then it will take a carrier signal and then modulate the signal using FSK
    (Frequency Shift Key).  Then the program will take the FSK signal and de-modulate it back to a analogue version of
     the binary string.
'''
signal = [0, 1, 1, 0, 1, 1, 1, 0]
original_signal = []


def display_digital_signal(binary, name):
    plt.figure(name)
    y = np.repeat(binary, 2, axis=None)
    t = np.arange(len(y))

    plt.step(t, y, 'r', linewidth=2)


def display_carrier_signal():
    plt.figure('Carrier Signal')

    x = np.linspace(0, 18 * np.pi, 201)
    plt.plot(x, np.sin(x))


def main():
    fsk = FSK(signal)
    display_carrier_signal()
    display_digital_signal(signal, 'Original Signal')
    fsk.encode_wave()

    original_signal = fsk.decode_wave()
    display_digital_signal(original_signal, 'De-Modulated Signal')

    plt.show()


if __name__ == '__main__':
    main()
