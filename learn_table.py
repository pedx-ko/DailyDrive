import time
import threading
from playsound import playsound
import os


def play_sound():
    # Replace the path below with the actual path to your sound file
    sound_file_path = os.getenv("SOUND_PATH")
    try:
        playsound(sound_file_path)
    except FileNotFoundError:
        print(f"Error: Sound file not found at {sound_file_path}")

while True:
    print("Next \n")
    play_sound()
    time.sleep(10)

sound_file_path = os.path.basename("C:\Windows\ding.wav") 
print(sound_file_path)