import tkinter as tk
import datetime
import time
from threading import Thread

#from nltk.sem.chat80 import continent
from pygame import mixer

# create object
root = tk.Tk()
root.geometry("500x250")

alarm_setting = False
current_thread = None

def alarm():
    # alarm set to an infinite loop
    global alarm_setting
    front_time()
    while alarm_setting:
        # alarm set
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        # get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"当前时间：{current_time}",f"闹钟时间：{set_alarm_time}")

        # condition to check if set time is equal to current time
        if current_time == set_alarm_time:
            print("Wake Up now!")
            # play sound continuously
            mixer.init()
            mixer.music.load("sound.wav")
            mixer.music.play(loops=5)


def stop_alarm():
    #global alarm_setting
    #global current_thread
    if mixer.get_init():
        mixer.music.stop()
    elif current_thread is not None:
        print("未到闹钟时间，无需停止！")


def threading():
    global alarm_setting
    global current_thread
    if current_thread is not None:
        pass
        #stop_alarm()
    else:
        alarm_setting = True
        current_thread = Thread(target=alarm)
        current_thread.start()

def front_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_clock.config(text = current_time)
    root.after(1000,front_time)



tk.Label(root, text="Alarm Clock", font="Helvetica 20 bold", fg="red").pack(pady=10)
tk.Label(root, text="Set Time", font="Helvetica 15 bold").pack()
time_clock= tk.Label(root,fg="red",font=("Arial", 24))
time_clock.pack(ipady=25, side=tk.TOP)


frame = tk.Frame(root)
frame.pack()

hour = tk.StringVar(root)
hours = [f"{i:02}" for i in range(24)]
hour.set(hours[0])

tk.OptionMenu(frame, hour, *hours).pack(side = tk.LEFT)

minute = tk.StringVar(root)
minutes = [f"{i:02}" for i in range(60)]
minute.set(minutes[0])

tk.OptionMenu(frame, minute, *minutes).pack(side = tk.LEFT)

second = tk.StringVar(root)
seconds = [f"{i:02}" for i in range(60)]
second.set(seconds[0])

tk.OptionMenu(frame, second, *seconds).pack(side = tk.LEFT)

tk.Button(root, text="Set Alarm", font="Helvetica 15", command=threading).pack(pady=20)

tk.Button(root, text="Stop Alarm", bg="red", fg="white", command=stop_alarm).pack(ipady=15, side=tk.BOTTOM)

def main():
    root.mainloop()

if __name__ == '__main__':
    main()