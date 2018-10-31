import time


# //计时装饰器
def timer(f):
    time.clock()
    f()
    how_long = time.clock()
    print(how_long)



@timer
def count():
    for i in range(1000, 10000):
        for j in range(999, 9999):
            k = i + j
