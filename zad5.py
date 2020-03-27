integers = [1, 2, 3, 4, 5, 6, 11, 12, 14, 23, 35, 41, 22, 11, 13, 17]

def map_and_filter(integers):
    print(list(map(lambda x: x, filter(lambda x: not list(filter(lambda y: x % y == 0, range(2, x))), integers))))

def list_comprehension(integrers):
    print([element for element in integers if all(element % y != 0 for y in range(2, element))])

def main():
    map_and_filter(integers)
    list_comprehension(integers)

if __name__ == '__main__':
    main()
