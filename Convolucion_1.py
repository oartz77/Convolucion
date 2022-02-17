import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import wave

file = wave.open('Still.wav')
audio = file.readframes(-1)
audio = np.frombuffer (audio, dtype=np.int16)

#plt.plot(audio)
#plt.title("Still")
#plt.show()

alfa = np.array([1.,0.,0.,0])
audio_modificado = np.convolve(audio, alfa)

audio_modificado = audio_modificado.astype(np.int16)
write('Still_modificado.wav', 40000, audio_modificado)

plt.plot(audio_modificado)
plt.title("Still_modificado")
plt.show()

