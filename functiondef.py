# Function definitions
def test_function():
    print("Test")


def test_list(li):
    for x in li:
        print(x)


def test_return(n):
    return n * 10


# Args
def test_args(x, y, z):
    print(x)
    print(y)
    print(z)


# Tuple
def test_tuple(*t):
    for i in t:
        print(i)


# Lambda
lamb = lambda x: x + 10


def test_lamb(x):
    return lambda y: x + y


m = test_lamb(5)

test_list("2")
test_return(10)
test_args(x=2, z=3, y=4)
test_tuple(10, 20, 30)
print(m(2))
