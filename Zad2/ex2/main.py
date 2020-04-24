from ex2.ex2.stack.finding_number_py import MinMaxStack


def main():
    stack = MinMaxStack()
    stack.push(20)
    stack.push(1)
    stack.push(15)

    print('Lowest number is:', end=' ')
    print(stack.lowest_number())

    print('Stack is:')
    while not stack.is_empty():
        print(stack.top(), end=' ')
        stack.pop()


if '__main__' == __name__:
    main()