count = 1  # 这里是声明的是全局变量，对于nonlocal来说全局变量是不包括的


def a():
    count = 'a函数里面'  # 这里对于nonlocal来说就是外面的函数已声明的变量

    def b():
        nonlocal count  # nonlocal count指的是函数b内
        print(count)
        count = 2

    b()
    print(count)


if __name__ == '__main__':
    a()
    print(count)
