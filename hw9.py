class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def show(self):
        print(f'({self.__x},{self.__y})', end='')

    def get(self):
        result = (self.__x, self.__y)
        return result

    def set(self, x, y):
        self.__x = x
        self.__y = y

class Rectangle:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        if x1 < x2 and y1 < y2:
            self.__lt = Point(x1,y1)
            self.__rb = Point(x2,y2)

        else:
            print('입력 형식이 맞지 않습니다. (x1 < x2 and y1 < y2)')
            self.__lt = Point(0,0)
            self.__rb = Point(0,0)

    def show(self):
        print("좌측 상단 꼭지점이 ", end='')
        self.__lt.show()
        print("이고 우측 상단 꼭지점이 ", end='')
        self.__rb.show()
        print("인 사각형 입니다.", end='')

    def getWidth(self):
        return self.__rb.get()[0]-self.__lt.get()[0]

    def getHeight(self):
        return self.__rb.get()[1]-self.__lt.get()[1]

    def getArea(self):
        return self.getWidth()*self.getHeight()

    def getPerimeter(self):
        return (self.getWidth()+self.getHeight())*2

def test():
    r1 = Rectangle(5, 5, 20, 10)
    a = r1.getArea()
    p = r1.getPerimeter()

    r1.show()
    print(f'\n넓이는 {a}, 둘레는 {p}')
    
if __name__ == '__main__':
    test()

    