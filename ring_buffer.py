import numpy as np


# A very *cough* "portable" *cough* ring buffer implementation.
# Can be used for implementing fixed delay lines.
class RingBuffer:

    # constructor
    def __init__(self, delay):
        self.delay = delay
        self.data = np.int16([0] * (delay + 1))
        self.read_index = 0
        self.write_index = self.read_index + delay

    # Returns read or write index incremented by 1, ensuring
    # that the index never goes out of the bounds of the buffer.
    #
    # @param index: number to increment.
    # @return: index, incremented by 1
    def _increment(self, index):
        # One would usually use modulo here, but a conditional
        # is actually faster than performing the mod operation
        # every time.
        if index + 1 > self.delay:
            return 0
        return index + 1

    # Returns read value from the ring buffer, and increments
    # the read position.
    #
    # @return: data value from current read position of buffer.
    def read(self):
        to_ret = self.data[self.read_index]
        self.read_index = self._increment(self.read_index)
        return to_ret

    # Writes value to the ring buffer, and increments the write
    # position.
    #
    # @param to_write: data to write to the buffer
    def write(self, to_write):
        self.data[self.write_index] = to_write
        self.write_index = self._increment(self.write_index)
