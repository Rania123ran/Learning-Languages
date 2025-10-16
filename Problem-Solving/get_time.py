import time ; 
def get_time():
    j = 0
    start_time = time.time()
    for i in range(100) :
        j +=1 
    end_time = time.time()
    t = end_time - start_time 
    print(t)
get_time()