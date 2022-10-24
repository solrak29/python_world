import random
import time
import logging
import threading
import concurrent.futures

#  code the plays around with threading and conditionals.
#  counts from 1 to 100 using two threads to count even or odd


odd_even_lock= threading.Lock()
isEven = threading.Condition()
isOdd  = threading.Condition()
count = 0

def is_odd() -> bool:
    global count
    logging.debug('checking odd')
    return ( count % 2 ) == 1

def is_even() -> bool:
    global count
    logging.debug('checking even')
    return ( count % 2 ) == 0

def odd():
    """ Mock getting message from the network """
    global count
    while count < 100:
        try:
            logging.debug('odd')
            while is_even():
                logging.debug('waiting odd')
                isOdd.wait()
            logging.info(count)
            count += 1
            isEven.notify()
        except Exception as e:
            logging.debug(f'odd {e}')


def even():
    """ Mock receiving and saving message """
    global count
    while count < 100:
        try:
            logging.debug('even')
            while is_odd():
                logging.debug('waiting even')
                isEven.wait()
            logging.info(count)
            count += 1
            isOdd.notify()
        except Exception as e:
            logging.debug(f'even {e}')


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt = "%H:%M:%S")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(even)
        executor.submit(odd)
