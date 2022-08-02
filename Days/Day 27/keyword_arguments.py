

def calculate(n, **kwargs):

    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])
    
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw["model"]

my_car = Car(make = "Nissan", model="GT-8")
print(my_car.model)

#The method .get() doesn't give error if key isn't found, returns None