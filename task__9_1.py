import time


class TrafficLight:
    __color: dict = {'red': 4, 'yellow': 2, 'green': 3}

    def running(self):
        for i in self.__color:
            print(i, f'{self.__color[i]} сек')
            time.sleep(self.__color[i])


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()