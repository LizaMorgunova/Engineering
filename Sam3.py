import datetime
import time
def display_time():
    for i in range(5):
        current_time = datetime.datetime.now()
        print(current_time.strftime("%H:%M:%S"))
        time.sleep(1)

if __name__ == "__main__":
    display_time()
