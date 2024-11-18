import tkinter as tk
import datetime
import time
from threading import Thread
import pygame
from pygame import mixer


# create object
root = tk.Tk()
root.geometry("500x250")


#def threading():
#    t1 = Thread(target=alarm)
#    t1.start()

alarm_setting = False
current_thread = None

def alarm():
    # alarm set to an infinite loop
    global alarm_setting
    while alarm_setting:
        # alarm set
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        # get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        # condition to check if set time is equal to current time
        if current_time == set_alarm_time:
            print("Wake Up now!")
            # play sound continuously
            mixer.init()
            mixer.music.load("sound.wav")
            mixer.music.play(loops=3)


def stop_alarm():
    global alarm_setting
    global current_thread
    try:
        if mixer.get_init():
            alarm_setting = False
            mixer.music.stop()
        elif current_thread is not None:
            current_thread.join()
            current_thread = None
    except pygame.error:
        print("闹钟尚未启动，无需停止！")
        #alarm_setting = False

    #if current_thread is not None:
        #current_thread.join()
        #current_thread = None

def threading():
    global alarm_setting
    global current_thread
    if current_thread is not None:
        stop_alarm()

    alarm_setting = True
    current_thread = Thread(target=alarm)
    current_thread.start()





tk.Label(root, text="Alarm Clock", font="Helvetica 20 bold", fg="red").pack(pady=10)
tk.Label(root, text="Set Time", font="Helvetica 15 bold").pack()

frame = tk.Frame(root)
frame.pack()

hour = tk.StringVar(root)
hours = [f"{i:02}" for i in range(24)]
hour.set(hours[0])

tk.OptionMenu(frame, hour, *hours).pack(side = tk.LEFT)
#hrs.pack(side = tk.LEFT)

minute = tk.StringVar(root)
minutes = [f"{i:02}" for i in range(60)]
minute.set(minutes[0])

tk.OptionMenu(frame, minute, *minutes).pack(side = tk.LEFT)
#mins.pack(side = tk.LEFT)

second = tk.StringVar(root)
seconds = [f"{i:02}" for i in range(60)]
second.set(seconds[0])

tk.OptionMenu(frame, second, *seconds).pack(side = tk.LEFT)
#secs.pack(side = tk.LEFT)

tk.Button(root, text="Set Alarm", font="Helvetica 15", command=threading).pack(pady=20)

tk.Button(root, text="Stop Alarm", bg="red", fg="white", command=stop_alarm).pack(ipady=15, side=tk.BOTTOM)

def main():
    root.mainloop()

if __name__ == '__main__':
    main()