from functools import wraps

def helper():
    try:
        raise Exception('Message')
        pass
    except Exception as Ex:
        print(Ex)
    else:
        print('else')
    finally:
        print('finally')

def zad9():
    with open('zad9.txt', 'r', encoding='UTF-8') as zad9:
        readed_txt = zad9.read()
        to_words = readed_txt.split()
        print('Wyrazów w dokumencie jest:')
        print(len(to_words))


def main():
    helper()
    zad9()

if __name__ == '__main__':
    main()

