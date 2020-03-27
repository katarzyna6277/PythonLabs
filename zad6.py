def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def main():
    fib()

if __name__ == '__main__':
    main()
