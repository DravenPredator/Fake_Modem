import matplotlib.pyplot as plt
import numpy as np
from FSK import FSK

'''
    Change signal to whatever you want as along as it contains 1's and 0's
'''
signal = [0, 1, 1, 0, 1, 1, 1, 0]
original_signal = []


def display_digital_signal(binary):
    plt.figure('Digital Signal')
    y = np.repeat(binary, 2, axis=None)
    t = np.arange(len(y))

    plt.step(t, (y + 2), 'r', linewidth=2)


def display_carrier_signal():
    plt.figure('Carrier Signal')

    x = np.linspace(0, 18 * np.pi, 201)
    plt.plot(x, np.sin(x))


def encode():
    fsk = FSK(signal)
    display_carrier_signal()
    display_digital_signal(signal)
    fsk.encode_wave()

    plt.show()


def decode():
    fsk = FSK(signal)
    original_signal = fsk.decode_wave()
    display_digital_signal(original_signal)



def main():
    encode()
    decode()


if __name__ == '__main__':
    main()
