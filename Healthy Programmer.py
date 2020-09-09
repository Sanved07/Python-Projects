from time import time
import datetime
from pygame import mixer

def music(file,s):
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        while True:
            a = input("s to stop ")
            if a == s:
                mixer.music.stop()
                break


def fl(nou):
    with open("fil.txt","a") as f:
        f.write(f"{nou} = {datetime.datetime.now()}\n")

if __name__ == '__main__':
    init_water= time()
    init_eyes= time()
    init_exercise= time()
    watersecs=3
    eyesecs=4
    exercise=5

    while True:
        if time()-init_water > watersecs:
            print("water drinking time")
            water = music(r"./mp3sforhealthyprogrammer/ocean.mp3","s")
            fl("water drank at")
            init_water=time()

        elif time()-init_eyes > eyesecs:
            print("eyes exercise time")
            water = music(r"./mp3sforhealthyprogrammer/eyes.mp3","s")
            fl("eyes relaxed at")
            init_eyes=time()

        elif time()-init_exercise >exercise:
            print("exercise time")
            water = music(r"./mp3sforhealthyprogrammer/playdate.mp3","s")
            fl("exercise done at")
            init_exercise=time()













