# create a car class that can brake, accelerate, drive, passengers

class Car():

    def __init__(self, manufacturer, model, pass_limit):
        self.name = manufacturer + " " + model
        self.pass_limit = pass_limit
        self.speed = 0
        self.passgr = []

    def brake(self):
        self.speed = 0
        print(f"{self.name} is stopped. It was a nice ride!")

    def drive(self, gear=1):
        self.speed = 10 * gear
        print(f"You're driving {self.name} at {self.speed} mp/h. Drive safe!")

    def add_pass(self, *args):
        for person in args:
            if len(self.passgr) < self.pass_limit:
                print(f'Accomodating {person}')
                self.passgr.append(person)
            else:
                print(f'Sorry,{person} cant be seated, all seats are '
                      'taken!')

    def remove_pass(self, *args):
        for person in args:
            try:
                self.passgr.remove(person)
                print(f'Bye {person}, it was nice to ride together!')
            except ValueError:
                print(f"There's no passenger {person} in the car")

car = Car('Lambo', 'Aventador 2020', 1)
car.drive(gear=10)
car.brake()
car.add_pass('Vasya', 'Petya', 'Masha')
car.remove_pass('SSS')
car.add_pass('Petya', 'Masha')
