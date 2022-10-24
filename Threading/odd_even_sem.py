import time
import logging
import threading
import concurrent.futures

#  code the plays around with threading and conditionals.
#  counts from 1 to 100 using two threads to count even or odd


odd_even_lock= threading.Lock()
isEven = threading.Semaphore(0)
isOdd  = threading.Semaphore(1)
count = 0

def odd():
    """ Mock getting message from the network """
    global count
    for count in range(1,100,2):
        try:
            logging.debug('odd')
            isOdd.acquire()
            logging.info(count)
            isEven.release()
        except Exception as e:
            logging.debug(f'odd {e}')


def even():
    """ Mock receiving and saving message """
    global count
    for count in range(2,100,2):
        try:
            logging.debug('even')
            isEven.acquire()
            logging.info(count)
            isOdd.release()
        except Exception as e:
            logging.debug(f'even {e}')


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt = "%H:%M:%S")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(even)
        executor.submit(odd)
