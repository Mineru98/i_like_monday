# -*- coding:utf-8 -*-
import os
import time
import schedule
import multiprocessing
from playsound import playsound

def play_monday():
    play = multiprocessing.Process(target=playsound, args=(os.path.join("assets", "spongebob.mp3"),))
    play.start()

schedule.every().monday.at('10:30').do(play_monday)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    while True:
        schedule.run_pending()
        time.sleep(1)