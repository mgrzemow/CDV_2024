import threading
import time

wyniki = {}

def czekaj(n):
    print('Watek', threading.current_thread().name, 'startuje z czasem', n)
    time.sleep(n)
    print(f'Watek {threading.current_thread().name} konczy pracę.\n', end='')
    wyniki[threading.current_thread().name] = 'wynik'


t1 = threading.Thread(target=czekaj, args=(7,), daemon=False)
t2 = threading.Thread(target=czekaj, args=(3,), daemon=False)
t3 = threading.Thread(target=czekaj, args=(5,), daemon=False)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(wyniki)