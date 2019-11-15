from shift_register import ShiftRegister


shift_reg = ShiftRegister(12)  # Create ShiftRegister object

vector = [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0]  # Test vector
length = len(vector)  # Test vector length

""" Simulation of writing to shift register"""
for i in range(len(vector)):
    shift_reg.serial_in(vector[length - i - 1])
    shift_reg.clk_rising_edge()
shift_reg.latch(0)  # Switch off latch
shift_reg.latch(1)  # Switch on latch

print("Input vector:\t" + str(vector))
print("Output vector:\t" + str(shift_reg) + "\n")

if vector == shift_reg.output_array:
    print("Vectors are equal!")
else:
    print("Vectors are not equal!")
