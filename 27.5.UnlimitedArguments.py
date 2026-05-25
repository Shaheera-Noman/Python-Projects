def add(*args):
    print(args)
    print(type(args))
    for n in args:
        print(n)

add(3, 4, 5)

def add(*args):
    print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum
print(add(5,2,5,5))
