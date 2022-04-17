import pyautogui as pg
import time
times = int(input("Enter countdown-\t"))
num = int(input("Enter number for how many \ntimes you should send msg-\t"))
msg = input("Type msg=\t")
for i in reversed(range(times)):
    print(f"program start in {i+1}")
    time.sleep(1)
for i in range(num):
    pg.write(msg)
    pg.press("Enter")

