import pyaudio
import wave
import struct
import math
from playsound import playsound
import time
import threading
import random
 
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 108000 #(60*60*30)
SLEEP_TIME = 5
WAVE_OUTPUT_FILENAME = "wave.wav"
DECIBEL_LIMIT = -15

class MyClass:
    not_waiting_for_sleep = True

def rms(data):
    count = len(data)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, data )
    sum_squares = 0.0
    for sample in shorts:
        n = sample * (1.0/32768)
        sum_squares += n*n
    return math.sqrt( sum_squares / count )
 
def main():
    audio = pyaudio.PyAudio()
    
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("recording...")
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        decibels = 20 * math.log10(rms(data))
        print("Decibels: " + str(decibels))
        if decibels > DECIBEL_LIMIT and decibels < -0.1 and MyClass.not_waiting_for_sleep:
            print("Vai dizer não")
            MyClass.not_waiting_for_sleep = False
            playsound(select_file())
            thread = threading.Thread(target=sleep, args=())
            thread.start()
        frames.append(data)
    print("finished recording")
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

def sleep():
    print("Vai dormir: " + str(MyClass.not_waiting_for_sleep))
    time.sleep(SLEEP_TIME)
    MyClass.not_waiting_for_sleep = True
    print("----------------------------------- Finished sleeping: " + str(MyClass.not_waiting_for_sleep) + "-------------------------------------")

def select_file():
    random_file = random.randint(1, 5)
    print("O ficheiro selecionado foi o :" + files[str(random_file)])
    return files[str(random_file)]

files = {
  "1": "nao_forte.wav",
  "2": "nao_forte_2.wav",
  "3": "nao_forte_3.wav",
  "4": "nao_forte_4.wav",
  "5": "nao_forte_5.wav"
}

main()
