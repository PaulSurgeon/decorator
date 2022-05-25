# Practice of decorator

def print_func(func):
    def inner():
        print("We are running function", func.__name__)
        func()
    return inner

def sayhi():
    print("hi")

sayhi = print_func(sayhi)
sayhi()


def timer(func):
    def inner():
        import time
        start = time.time()
        func()
        end = time.time()
        elapse = end - start
        print("elapsing", elapse, "seconds")
    return inner


def sayhi2():
    print("hello hi")
    count = 0
    for i in range(10000000):
        count += 1
    print(count)

sayhi2 = timer(sayhi2)
sayhi2()
