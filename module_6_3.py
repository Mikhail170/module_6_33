class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        '''увеличивает пройденный путь по координате х'''
        self.x_distance += dx


class Eagle:
    def __init__(self):
        super().__init__()
        self.y_distance = 0
        self.sound = 'I train, eat, sleep and repeat'

    def fly(self, dy):
        '''увеличивает проденный путь по координате у'''
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        '''запускает методы run и fly для увеличения дистанции'''
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        '''показывает текущее положение объекта'''
        return self.x_distance, self.y_distance

    def voice(self):
        '''печатает звук пегаса'''
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()