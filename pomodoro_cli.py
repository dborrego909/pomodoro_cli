# Create pomodoro timer

#ingrained 25 min study timer then 5 min break timer

import time


start = input("Type START or STOP to start or stop the timer")


while True:
    if start == "start" or "stop":
        print("working")
    else:
        print("incorrect input")
        return False
#timer():

