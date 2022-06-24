# -*- coding:utf-8 -*-
import os
import time
import pathlib
import schedule
import multiprocessing
from playsound import playsound

def play_monday():
    play = multiprocessing.Process(target=playsound, args=(os.path.join(pathlib.Path(__file__).parent.absolute(), "assets", "spongebob.mp3"),))
    play.start()

schedule.every().monday.at('10:30').do(play_monday)
schedule.every().friday.at('20:58').do(play_monday)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    while True:
        schedule.run_pending()
        time.sleep(1)