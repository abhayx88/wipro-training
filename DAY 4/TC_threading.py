import threading

def task(name):
    print(f"{name} is running")

t1 = threading.Thread(target=task, args=("Thread1",))
t2 = threading.Thread(target=task, args=("Thread2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Main thread ends")
