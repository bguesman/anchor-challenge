# usage: python channel_delay.py <file-path.wav> <sample-rate (integer)> <output-path.wav>
# Adds a delay of 0.1s to PCM data at file-path, assuming sample rate of
# sample-rate, and writes to output-path.wav. Assumes file-path.wav is an
# interleaved stereo PCM file of 16-bit precision with no header data.

import sys
import struct
from ring_buffer import RingBuffer

# ensure we have the right number of args
if len(sys.argv) != 4:
    print('usage: python channel_delay.py <file-path.wav> <sample-rate (integer)> <output-path.wav>')
    sys.exit()

# get the args
in_file = sys.argv[1]
sample_rate = int(sys.argv[2])
out_file = sys.argv[3]

# calculate the delay to apply in samples
delay = int(0.1 * sample_rate)

# set up the ring buffer to implement the delay line
buffer = RingBuffer(delay)

with open(in_file, 'rb') as in_file_stream:
    with open(out_file, 'wb') as out_file_stream:
        left = in_file_stream.read(2)
        right = in_file_stream.read(2)
        while left and right:
            # allow left channel to pass through unchanged
            out_file_stream.write(left)
            # but delay the right channel
            buffer.write(struct.unpack('h', right)[0])
            out_file_stream.write(struct.pack('h', buffer.read()))
            # perform the next read
            left = in_file_stream.read(2)
            right = in_file_stream.read(2)
        # ensure that the buffer empties before we're done
        for i in range(delay):
            out_file_stream.write(struct.pack('h', 0))
            out_file_stream.write(struct.pack('h', buffer.read()))
