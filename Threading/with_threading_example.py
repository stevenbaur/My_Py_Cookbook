import threading
import time

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second..')
    time.sleep(1)
    print('Done sleeping..')

thread_one = threading.Thread(target=do_something)
thread_two = threading.Thread(target=do_something)

thread_one.start()
thread_two.start()

thread_one.join()           #sorgt dafür, dass die funktionen fertig sind,
thread_two.join()           #BEVOR der Restcode ausgeführt wird. Sonst ist finish Time = 0..

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')


"""
Programm startet den ersten Thread, der die Funktion aufruft zeitgleich mit dem zweiten Thread, der
ebenfalls die Funktion aufruft.
Beide laufen somit parallel ab. Erst wenn die Funktionen completed sind (thread.join()), wird der restliche Code,
also die Zeitmessung Zeile 20 durchgeführt.
Output:

Sleeping for 1 second..
Sleeping for 1 second..
Done sleeping..Done sleeping..

Finished in 1.0 second(s)

Process finished with exit code 0



-----------------time---------------->
       1 Second         |
       ^       1 Second |
       |       ^        |
       |       |        v
func()   func()          Done.
"""