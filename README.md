# MidiController

The goal of the project is to create and test an extension board with two SIPO 74HC595 shift registers.
The system will work with Arduino Uno.

The registers function is to expand the number of input and output ports of the Arduino board. The whole will work as a controller for the MIDI keyboard.

The use of shift registers allows you to use every available keyboard.

There are two version of the board: 1. Board with additional connections and LED diodes to observe input and outputs
                                    2. Board without connections and LEDs

Tests has been manually executed in NI TestStand. The board was connected via NI myRIO.

## Board without testpoints:

<img src="https://github.com/Fysek/MidiController/blob/master/Photos/Schematic.PNG" width="600"/>
<img src="https://github.com/Fysek/MidiController/blob/master/Photos/Board.PNG" width="600"/>

## Board with testpoints:
<img src="https://github.com/Fysek/MidiController/blob/master/Photos/Schematic_test.PNG" width="600"/>
<img src="https://github.com/Fysek/MidiController/blob/master/Photos/Board_test.PNG" width="600"/>
