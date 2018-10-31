import time


def insure_user(fun):
    user = 'jiao'
    pwd = 'jiao'
    username = input('please input your name>>>')
    password = input('please input your password>>>')
    if username == user and password == pwd:
        print('login success')
        fun()
    else:
        print('error')


@insure_user
def count():
    def count_time(f):
        time.clock()
        result = f()
        timer = time.clock()
        print('用时：', timer, '\n总计:', result)

    @count_time
    def timer_long():
        z = 0
        for i in range(1, 10000):
            for j in range(1, 10000):
                z += i + j
        return z
