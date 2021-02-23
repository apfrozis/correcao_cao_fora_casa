import librosa

class ZeroCrossingRateService:

    def __init__(self, audio_file):
        self.audio_file = audio_file

    def zero_crossing_rate_calculation(self):
        y, sr = librosa.load('wave.wav')
        array = librosa.feature.zero_crossing_rate(y)
        print('oi')

