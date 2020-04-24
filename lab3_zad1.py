# 1. Używając klas zdefiniuj:
# a. iterator, który będzie generował kolejne liczby Fibonacciego (iterator jest
# również tutaj obiektem iterowalnym),
# b. dekorator, który zliczy wystąpienia wywołań funkcji.

from functools import wraps


class MyDeco:
    def __init__(self, func):
        self.__func = func
        # wraps(self.__func)
        self.__calls = 0

    def __call__(self, *args, **kwargs):
        self.__calls += 1
        print('Ilosc wystąpien funkcji:', self.__calls)
        return self.__func(*args, **kwargs)


class Fibonacci():
    def __init__(self, n):
        self.counter = n
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == 0:
            raise StopIteration

        self.counter -= 1

        a_plus_b = self.a + self.b
        self.a = self.b
        self.b = a_plus_b

        return self.a


@MyDeco
def fibonacci_call(n):
    fib = Fibonacci(n)

    for fib in fib:
        print(fib)


def main():
    fibonacci_call(20)
    fibonacci_call(3)
    fibonacci_call(5)


if '__main__' == __name__:
    main()
