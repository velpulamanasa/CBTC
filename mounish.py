import pyaudio
import wave

audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)


frame = []
try:
    print("Recording ............ Press ctrl+c to stop the recording")
    while True:
        data = stream.read(1024)
        frame.append(data)
except KeyboardInterrupt:
    print("Recording ... has been stopped..")

stream.stop_stream()
stream.close()
audio.terminate()


sound_file = wave.open("myrecording.wav","wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frame))
sound_file.close()
