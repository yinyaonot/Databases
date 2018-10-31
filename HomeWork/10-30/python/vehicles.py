'''
类
    车辆 Vehicles
        属性
            商标 brand(str)
            颜色 color(str)
        方法
            行驶  run         我已经开动了
                show_info  在控制台显示商标和颜色
    小汽车 Car
        继承 Vehicles
        属性
            座位seats(int)
        方法
            show_car 在控制台显示小汽车的信息
    卡车 Truck
        属性
            载重  load(float)
        方法
            show_truck


要求  编写构造方法,初始化成员属性

'''


class Vehicles():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def run(self):
        print('我已经开动了')

    def show_info(self):
        print('商标:%s \n颜色:%s' % (self.brand, self.color))


class Car(Vehicles):
    def __init__(self, brand, color, seats):
        Vehicles.__init__(self, brand, color)
        self.seats = seats

    def show_car(self):
        print('商标:%s \n颜色:%s\n座位数:%d' % (self.brand, self.color, self.seats))


class Truck(Vehicles):
    def __init__(self, brand, color, loads):
        Vehicles.__init__(self, brand, color)
        self.loads = loads

    def show_truck(self):
        print('商标:%s \n颜色:%s\n载重量:%.2f 吨' % (self.brand, self.color, self.loads))


if __name__ == '__main__':
    cars = Car('大众', '白色', 5)
    cars.show_car()
    print()
    truck = Truck('五菱重工', '亮银色', 2)
    truck.show_truck()
