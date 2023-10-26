def sum(a, b):
    return a + b


def sum_and_print(a, b):
    print('executing sum...')
    result = sum(a, b)
    print('execition completed.')
    return result


if __name__ == '__main__':
    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(sum(a, b))
