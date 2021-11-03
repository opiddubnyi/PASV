# -*- coding: utf-8 -*-

class Engine:

    def move(self):
        print("I'm moving")

    def stop(self):
        print("I'm standing")

class Camera:
    def look(self):
        print("I'm watching")

class Cleaner:
    def clean(self):
        print("I'm cleaning")

class RobotVacuum(Engine, Camera, Cleaner):
    def __init__(self, name):
        self.name = name
        print(f"Hello, I'm {self.name}")

robot1 = RobotVacuum('Wally')
robot1.move()
robot1.stop()
robot1.look()
robot1.clean()
