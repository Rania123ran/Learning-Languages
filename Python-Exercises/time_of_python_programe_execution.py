import time
start = time.time()
s = 0 
for i in range(400000):
     s += i 
end = time.time()
print(end-start)