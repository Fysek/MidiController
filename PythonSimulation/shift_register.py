class ShiftRegister:

    def __init__(self, length):
        self.length = length
        self.__latch = 1
        self.__serial_bit = 0
        self.__shift_array = []
        self.output_array = []
        for i in range(length):
            self.__shift_array.append(0)
            self.output_array.append(0)

    def serial_in(self, bit):
        if bit is 0:
            self.__serial_bit = 0
        else:
            self.__serial_bit = 1

    def clk_rising_edge(self):
        for i in range(0, self.length - 1):
            self.__shift_array[self.length - 1 - i] = self.__shift_array[self.length - 2 - i]
        self.__shift_array[0] = self.__serial_bit
        if self.__latch is 0:
            self.__write_to_output()

    def latch(self, bit):
        if bit is 0:
            self.__latch = 0
            self.__write_to_output()
        else:
            self.__latch = 1

    def __write_to_output(self):
        for i in range(self.length):
            self.output_array[i] = self.__shift_array[i]

    def __str__(self):
        return str(self.output_array)
