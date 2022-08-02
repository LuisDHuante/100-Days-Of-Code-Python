#Unlimited positional arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
        
print(add(2,3,5,6))

