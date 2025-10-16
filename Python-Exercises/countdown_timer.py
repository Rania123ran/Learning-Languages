import time
t = int(input("Enter the time in seconds :"))
for rest in range(t,0,-1):
    hour = rest//3600
    min = (rest%3660)//60
    sec = rest % 60
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)
print("Time's up")