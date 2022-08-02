from random import randint

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.


def make_pie(index):
    try:
        fruit = fruits[index]

    except IndexError:
        print("Fruit pie")
    
    else:
        print(f"{fruit} pie")

make_pie(randint(0, 3))