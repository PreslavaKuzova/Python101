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

import datetime
def log(file_name):
    def inner_wrapper(func):
        def accepter():
            def log():
                with open (file_name, 'w') as f:
                    f.write(func.__name__ + ' was called at ' + str(datetime.datetime.now()))
                return log()
            return func()
        return accepter
    return inner_wrapper

# def log():
#     with open (file_name, 'w') as f:
#         f.write(func.__name__ + ' was called at ' + str(datetime.datetime.now()))
# return log

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"

def main():
    print(say_hello('Preslava'))
    print(get_low())


if __name__ == '__main__':
    main()
