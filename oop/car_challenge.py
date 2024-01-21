class Car:
    def __init__(self, speed=120, maxSpeed=200):
        self.speed = speed
        self.maxSpeed = maxSpeed

    def accelerate(self, incraseSpeed=5):
        maxSpeed = self.maxSpeed
        newSpeed = self.speed + incraseSpeed
        self.speed = newSpeed if newSpeed <= maxSpeed else maxSpeed
        return self.speed

    def stop(self, delta=5):
        if (self.speed < 0):
            self.speed = 0
        else:
            self.speed -= delta
        return self.speed

    def __str__(self):
        return (f'Current speed: {self.speed}, Max Speed: {self.maxSpeed}')


if __name__ == '__main__':
    c1 = Car(speed=180)

    for _ in range(5):
        print(c1.accelerate())

    for _ in range(2):
        print(c1.stop())

    print(c1)
