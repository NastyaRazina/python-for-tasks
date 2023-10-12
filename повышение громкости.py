import wave
import struct


def tweak_audio(frame, count):
    frame *= count
    if frame <= -32768:
        return -32768
    elif frame >= 32767:
        return 32767
    return frame


volume_adjustment = 100
input_audio = wave.open("in.wav", mode="rb")
output_audio = wave.open("in.wav", mode="wb")
output_audio.setparams(input_audio.getparams())

num_frames = input_audio.getnframes()
audio_data = struct.unpack("<" + str(num_frames) + "h", input_audio.readframes(num_frames))
adjusted_audio_data = list(map(lambda frame: tweak_audio(frame, volume_adjustment), audio_data))
packed_audio_data = struct.pack("<" + str(len(adjusted_audio_data)) + "h", *adjusted_audio_data)
output_audio.writeframes(packed_audio_data)

input_audio.close()
output_audio.close()
