import random
import time
from threading import Thread
import multiprocessing
import numpy


too_large_array = numpy.array([random.randint(1, 9) for i in range(27999999)])
too_large_list = too_large_array.tolist()

#генерируем массив, везде будем считать количестово вхождений числа 2

def simple_search():
    total = 0
    for elem in range(27999999):
        if too_large_list[elem] == 2:
            total += 1
    return total

start_time = time.time()
print(simple_search())
end_time = time.time()
print(end_time - start_time, "seconds in one thread")


print("")

# считаем то же самое в трех потоках

total_in_threads = 0
def search_for_thread(diapason):
    total = 0
    for elem in range(9333333):
        if too_large_list[elem + diapason] == 2:
            total += 1
    global total_in_threads
    total_in_threads += total
    return total

time_start_3_thread = time.time()
tasks = []

for i in range(3):
    if i == 0:
        diap = 0
        th = Thread(target=search_for_thread, args=(diap, ))
        tasks.append(th)
    if i == 1:
        diap = 9333333
        th = Thread(target=search_for_thread, args=(diap, ))
        tasks.append(th)
    if i == 2:
        diap = 18666666
        th = Thread(target=search_for_thread, args=(diap, ))
        tasks.append(th)

for task in tasks:
    task.start()

for task in tasks:
    task.join()
time_stop_3_thread = time.time()
print(total_in_threads)
print(time_stop_3_thread - time_start_3_thread, "seconds in 3 threads")


print("")

# а теперь в трех процессах

manager = multiprocessing.Manager()
total_in_proc = manager.list()
def search_for_proc(diapason):
    total = 0
    for elem in range(9333333):
        if too_large_list[elem + diapason] == 2:
            total += 1
    total_in_proc.append(total)
    return total

time_start_3_proc = time.time()
procs = []

for p in range(3):
    if p == 0:
        diap = 0
        pr = multiprocessing.Process(target=search_for_proc, args=(diap, ))
        procs.append(pr)
    if p == 1:
        diap = 9333333
        pr = multiprocessing.Process(target=search_for_proc, args=(diap, ))
        procs.append(pr)
    if p == 2:
        diap = 18666666
        pr = multiprocessing.Process(target=search_for_proc, args=(diap, ))
        procs.append(pr)

for process in procs:
    process.start()

for process in procs:
    process.join()
time_stop_3_proc = time.time()
print(sum(total_in_proc))
print(time_stop_3_proc - time_start_3_proc, "seconds in 3 process")

