import time
import random
while True:
    
    channel=list(range(1,4))
    x=random.choice(channel)
    f= ".00"+str(x)
    x=float(f)
    time.sleep(x)
    print("This prints after ",x)