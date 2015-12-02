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
signal = []
original_signal = []


def validate_input_string(string):
    signal_wave = []
    for element in range(len(string)):
        if int(string[element]) != 1 and int(string[element]) != 0:
            input = raw_input('YOUR INPUT IS INVALID!\nPlease enter in a string of 1 and 0:\n')
            validate_input_string(input)
            break
        else:
            signal_wave.append(int(string[element]))

    return signal_wave


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
    test_string = raw_input('Please enter in a binary string:\n')
    signal = validate_input_string(test_string)

    fsk = FSK(signal)
    display_carrier_signal()
    display_digital_signal(signal, 'Original Signal')
    fsk.encode_wave()

    original_signal = fsk.decode_wave()
    display_digital_signal(original_signal, 'De-Modulated Signal')

    plt.show()


if __name__ == '__main__':
    main()
