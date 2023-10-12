import wave
import struct


def tweak(frame, count):
    frame *= count
    if frame <= -32768:
        return -32768
    elif frame >= 32767:
        return 32767
    return frame


n = 100
source = wave.open("in.wav", mode="rb")
dest = wave.open("out.wav", mode="wb")
dest.setparams(source.getparams())
frames_count = source.getnframes()
data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
newdata = list(map(lambda frame: tweak(frame, n), data))
newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
dest.writeframes(newframes)
source.close()
dest.close()
