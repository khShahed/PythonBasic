import time

while True:
    userInput = input(">> ")
    try:
        when_to_stop = abs(int(userInput))
    except KeyboardInterrupt:
        break
    except:
        print("Not a number.")
    while when_to_stop >= 0:
        min, sec = divmod(when_to_stop, 60)
        hour, min = divmod(min, 60)
        time.sleep(1)
        time_left = "{:02}:{:02}:{:02}".format(hour, min, sec)
        print(time_left +"\r", end="")
        when_to_stop-=1
    print()

