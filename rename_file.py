import os
import pathlib
import pdb

for filename in os.listdir(str(pathlib.Path().absolute()) + '/audio_files_to_test_ann'):
    if filename.endswith(".wav"):
        path = str(pathlib.Path().absolute()) + '/audio_files_to_test_ann/'
        os.rename(path + filename,path + filename.split('.')[0] + '_bark.wav')