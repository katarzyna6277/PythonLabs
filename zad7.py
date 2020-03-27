#7. Zaimplementuj dekorator, który wypisze nazwę i argumenty wywołanej funkcji.
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args):
        print('Argumenty to:')
        print(args)
        print('Nazwa funkcji to:')
        print(func.__name__)
        return func(*args)
    return wrapper


@my_decorator
def f(*args):
    a = 10


def main():
    f(1,23,4)


if __name__ == '__main__':
    main()


