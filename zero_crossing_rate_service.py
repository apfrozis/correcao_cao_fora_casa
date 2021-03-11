import librosa
import sys
import pdb
import os

# Import only to call class - delete after
import pathlib


# from zero_crossing_rate_service import ZeroCrossingRateService
# ZeroCrossingRateService('nao_forte.wav').zero_crossing_rate_calculation()
# from importlib import reload
# import pathlib
# ZeroCrossingRateService.create_csv(str(pathlib.Path().absolute()) + '/audio_files_to_test_ann')
# pdb.set_trace()

class ZeroCrossingRateService:

    def zero_crossing_rate_calculation(self, audio_file):
        y, sr = librosa.load(audio_file)
        array = librosa.feature.zero_crossing_rate(y)
        return array[0]


    def create_csv(dir):
        for filename in os.listdir(dir):
            if filename.endswith(".wav"):
                if filename.endswith("bark.wav"):
                    bark = 1
                else:
                    bark = 0
                print(os.path.join(dir, filename))
                y, sr = librosa.load(os.path.join(dir, filename))
                array = librosa.feature.zero_crossing_rate(y)
                try:
                    with open("zero_crossing_rate_info.csv", "a") as zero_crossing_rate_info:
                        zero_crossing_rate_info.write(','.join(str(x) for x in array[0]) + ',' + str(bark) + '\n')
                except:
                    e = sys.exc_info()
                    pdb.set_trace()
                    print( "Error: %s" % e )

ZeroCrossingRateService.create_csv(str(pathlib.Path().absolute()) + '/audio_files_to_test_ann')

