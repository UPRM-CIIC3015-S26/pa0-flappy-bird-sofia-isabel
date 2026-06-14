import wave
import math
import struct

filename = "score.wav"
duration = 0.2
frequency = 700
sample_rate = 44100

with wave.open(filename, "w") as sound_file:
    sound_file.setnchannels(1)
    sound_file.setsampwidth(2)
    sound_file.setframerate(sample_rate)

    for i in range(int(duration * sample_rate)):
        value = int(32767 * 0.5 * math.sin(2 * math.pi * frequency * i / sample_rate))
        sound_file.writeframes(struct.pack("<h", value))

print("score.wav created!")