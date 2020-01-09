import time

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second..')
    time.sleep(1)
    print('Done sleeping..')

do_something()
do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

"""
Programm startet die erste Funktion, wenn diese beendet ist, startet erst die zweite Funktion.
Das heißt, in den sleep-pausen wird einfach _nichts_ getan.
Output:

Sleeping for 1 second..
Done sleeping..
Sleeping for 1 second..
Done sleeping..
Finished in 2.0 second(s)

Process finished with exit code 0



-----------------time---------------->
       1 Second        1 Second
       ^       |      ^        |
       |       v      |        v
func()          func()          Done.
"""