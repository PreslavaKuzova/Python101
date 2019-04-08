import datetime
import time

def accepts(*types):
    def accepter(func):
        def decorated(*args_function):
            sub_string = [type(i) for i in args_function]
            
            if all(x in sub_string for x in list(types)):
                return func(*args_function)
            raise Exception("Error")
        return decorated
    return accepter

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
def encrypt(key):
    def accepter(func):
        def encpyption():
            ciphertext = ""
            for c in (func()).upper():
                if c.isalpha(): 
                    ciphertext += I2L[ (L2I[c] + key)%26 ]
                else: 
                    ciphertext += c
            return ciphertext
        return encpyption
    return accepter

def log(file_name):
    def decorator(func):
        def accepter():
            with open (file_name, 'a') as f:

                f.write(func.__name__ + ' was called at ' + str(datetime.datetime.now()) + '\n')
            return func()
        return accepter
    return decorator

def performance(file_name):
    def decorator(func):
        def accepter():
            start = time.time()
            func()
            end = time.time()
            with open (file_name, 'a') as f:
                f.write(func.__name__ + ' was called and took ' + str(end - start))
            return func()
        return accepter
    return decorator

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"

@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"

def main():
    print(say_hello('Preslava'))
    # print(get_low())
    something_heavy()

if __name__ == '__main__':
    main()
