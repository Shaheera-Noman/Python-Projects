def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
add(3, 4, 5)

def calculate(n, **kwargs):
    print(kwargs)
    # print(type(kwargs))
    # print(kwargs["add"])
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=4, multiply=5)

class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

# my_car = Car(make="Honda Civic", model= "Type R 1799cc")
my_car = Car(make="Honda Civic")
print(my_car.model)