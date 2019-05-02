from contextlib import ContextDecorator, contextmanager
from datetime import datetime
import time


#this can be implemented with a class with functions __init__, __enter__ and __exit__
@contextmanager
def performace(filename):
    #works like __enter__
    start_time = time.time()
    
    #the point where the things get different is where the yield is 
    yield

    #works like the __exit__
    with open(filename, 'a') as f:
        f.write('Date: ' + str(datetime.now()) + ' Execution time: ' + str(time.time() - start_time) + '\n')

# conterxt managers work like functions for checks
@contextmanager
def assertRaisesFunc(exception, message = None):
    try:
        yield
    except Exception as ex:
        if exception == type(ex):
            print('Congrats')

            return
        else:
            raise Exception('Different exception')
    else:
        raise Exception('No exceptions')

class assretRaises():
    def __init__(self, expected_exception_class, message = None):
        self.expected_exception_class = expected_exception_class
        self.message = message

    def __enter__(self):
        pass

    def __exit__(self, exception_class, exc, shano):
        if not exc:
            raise Exception('Exception not found')

        if self.expected_exception_class == exception_class:
            if self.message is not None and self.message == str(exc):
                return True
            else:
                raise Exception('Message is wrong')
        
        if exc:
            raise Exception('Exception found but it is not {exc}'.format(exc = self.expected_exception_class))

        return False

def test1():
    with performace('log_file.txt'):
        time.sleep(5)

def test2():
    with assertRaisesFunc(ZeroDivisionError, 'shano'):
        1//0

test2()

# def some_generator():

#     yield 1
    
#     yield 2

#     yield 3
    
#     yield 4

# for i in some_generator():
    # pass