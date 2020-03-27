# 8. Zaimplementuj dekorator, który zliczy i wypisze na standardowe wyjście liczbę wywołań danej funkcji,
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print('ilosc zliczen', wrapper.calls)
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


@my_decorator
def f(element):
    return element


def main():
    for i in range(5):
        (f(i))


if __name__ == '__main__':
    main()
