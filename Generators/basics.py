def basic():
    yield "Value 1"
    yield "Value 2"
    yield "Value 3"
    yield "Value 4"

test = basic()
 
for trial in test:
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))