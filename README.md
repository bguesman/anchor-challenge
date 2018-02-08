# anchor-challenge
Coding challenge for anchor.fm. Python script that delays one channel (in this case, the right channel) of a stereo 16-bit .raw file by 0.1s, given a specified sample rate.

The implementation uses a simple fixed delay line, implemented using a ring buffer. Specifically, I'm referring to the RingBuffer class in ring_buffer.py. The underlying data structure of the buffer is a numpy array of 16-bit integers, though other choices like a vanilla list would likely work just as well.

At the moment, the script is only capable of performing one task-delaying the right channel by 0.1 seconds. That said, it could easily be extended to delay either channel by any specified amount of time, or to implement other common delay line features like feedback or mix.
