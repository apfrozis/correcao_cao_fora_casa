import pyaudio
import wave
import struct
import math
from playsound import playsound
import time
import asyncio
import threading

def sleep():
    print("antes do sleep")
    time.sleep(1)
    print("depois sleep")
 

def main():
    print("antes de chamar o metodo")
    thread = threading.Thread(target=sleep, args=())
    thread.start()
    print("depois de chamar o metodo")

main()