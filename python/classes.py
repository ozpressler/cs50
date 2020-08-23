class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(7, 11)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight1 = Flight(2)

people = ["Oz", "Aya", "Bobby"]
for person in people:
    if flight1.add_passanger(person):
        print(f"{person} was added to the flight!")
    else:
        print(f"Unsuccessful, no open seats for {person}.")