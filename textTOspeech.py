!pip install gTTS

from gtts import gTTS
from IPython.display import Audio
audio1 = gTTS('An interesting short project for MLH')
audio1.save('1.wav')
sound_file = '1.wav'
Audio(sound_file, autoplay=True)
